using System;
using System.Collections.Generic;
using System.Security.Claims;
using System.Threading.Tasks;
using AgriSaarthi.Api.Data;
using AgriSaarthi.Api.Models;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AgriSaarthi.Api.Controllers
{
    public class AccountController : Controller
    {
        private readonly AgriSaarthiDbContext _context;

        public AccountController(AgriSaarthiDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult Login(string? returnUrl = null)
        {
            if (User.Identity?.IsAuthenticated == true)
            {
                return RedirectToAction("Dashboard", "Home");
            }

            ViewData["ReturnUrl"] = returnUrl;
            return View(new LoginViewModel());
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Login(LoginViewModel model, string? returnUrl = null)
        {
            if (!ModelState.IsValid)
            {
                return View(model);
            }

            var farmer = await _context.Farmers.FirstOrDefaultAsync(f => f.Email.ToLower() == model.Email.ToLower());

            if (farmer == null || !BCrypt.Net.BCrypt.Verify(model.Password, farmer.PasswordHash))
            {
                model.ErrorMessage = "Invalid email address or password. Please verify your credentials.";
                return View(model);
            }

            var claims = new List<Claim>
            {
                new Claim(ClaimTypes.NameIdentifier, farmer.Id.ToString()),
                new Claim(ClaimTypes.Name, farmer.FullName),
                new Claim(ClaimTypes.Email, farmer.Email),
                new Claim("PhoneNumber", farmer.PhoneNumber)
            };

            var claimsIdentity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);
            var authProperties = new AuthenticationProperties
            {
                IsPersistent = model.RememberMe,
                ExpiresUtc = DateTimeOffset.UtcNow.AddDays(7)
            };

            await HttpContext.SignInAsync(
                CookieAuthenticationDefaults.AuthenticationScheme,
                new ClaimsPrincipal(claimsIdentity),
                authProperties);

            if (!string.IsNullOrEmpty(returnUrl) && Url.IsLocalUrl(returnUrl))
            {
                return Redirect(returnUrl);
            }

            return RedirectToAction("Dashboard", "Home");
        }

        [HttpGet]
        public IActionResult Register()
        {
            if (User.Identity?.IsAuthenticated == true)
            {
                return RedirectToAction("Dashboard", "Home");
            }

            return View(new RegisterViewModel());
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Register(RegisterViewModel model)
        {
            if (!ModelState.IsValid)
            {
                return View(model);
            }

            var existingEmail = await _context.Farmers.AnyAsync(f => f.Email.ToLower() == model.Email.ToLower());
            if (existingEmail)
            {
                model.ErrorMessage = "An account with this email address already exists. Please sign in.";
                return View(model);
            }

            var existingPhone = await _context.Farmers.AnyAsync(f => f.PhoneNumber == model.PhoneNumber);
            if (existingPhone)
            {
                model.ErrorMessage = "An account with this phone number already exists.";
                return View(model);
            }

            var hashedPassword = BCrypt.Net.BCrypt.HashPassword(model.Password);

            var newFarmer = new Farmer
            {
                FullName = model.FullName,
                Email = model.Email.Trim().ToLower(),
                PhoneNumber = model.PhoneNumber.Trim(),
                PasswordHash = hashedPassword,
                CreatedAt = DateTime.UtcNow,
                Profile = new FarmerProfile
                {
                    Location = "Punjab, India",
                    State = "Punjab",
                    District = "Kapurthala",
                    FarmSize = 4.0,
                    SoilType = "Alluvial Loam",
                    IrrigationType = "Canal / Tube Well",
                    PrimaryCrop = "Wheat & Rice",
                    CreatedAt = DateTime.UtcNow,
                    UpdatedAt = DateTime.UtcNow
                }
            };

            _context.Farmers.Add(newFarmer);
            await _context.SaveChangesAsync();

            // Automatically sign in the farmer upon successful registration
            var claims = new List<Claim>
            {
                new Claim(ClaimTypes.NameIdentifier, newFarmer.Id.ToString()),
                new Claim(ClaimTypes.Name, newFarmer.FullName),
                new Claim(ClaimTypes.Email, newFarmer.Email),
                new Claim("PhoneNumber", newFarmer.PhoneNumber)
            };

            var claimsIdentity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);
            await HttpContext.SignInAsync(
                CookieAuthenticationDefaults.AuthenticationScheme,
                new ClaimsPrincipal(claimsIdentity),
                new AuthenticationProperties { IsPersistent = true });

            return RedirectToAction("Dashboard", "Home");
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Logout()
        {
            await HttpContext.SignOutAsync(CookieAuthenticationDefaults.AuthenticationScheme);
            return RedirectToAction(nameof(Login));
        }
    }
}
