using System;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using AgriSaarthi.Api.Data;
using AgriSaarthi.Api.Models;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AgriSaarthi.Api.Controllers
{
    public class HomeController : Controller
    {
        private readonly AgriSaarthiDbContext _context;

        public HomeController(AgriSaarthiDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult Index()
        {
            if (User.Identity?.IsAuthenticated == true)
            {
                return RedirectToAction(nameof(Dashboard));
            }
            return RedirectToAction("Login", "Account");
        }

        [Authorize]
        [HttpGet]
        public async Task<IActionResult> Dashboard()
        {
            var farmerIdStr = User.FindFirstValue(ClaimTypes.NameIdentifier);
            Farmer? farmer = null;

            if (int.TryParse(farmerIdStr, out int fid))
            {
                farmer = await _context.Farmers
                    .Include(f => f.Profile)
                    .FirstOrDefaultAsync(f => f.Id == fid);
            }

            // Fallback to first farmer in DB if claim not matched
            farmer ??= await _context.Farmers.Include(f => f.Profile).FirstOrDefaultAsync();

            var latestAdvisory = await _context.CropAdvisories
                .OrderByDescending(c => c.RequestDate)
                .FirstOrDefaultAsync();

            var marketPrices = await _context.MarketPrices
                .OrderBy(m => m.Commodity)
                .Take(6)
                .ToListAsync();

            var model = new DashboardViewModel
            {
                FarmerName = farmer?.FullName ?? "Taman Preet Singh",
                Email = farmer?.Email ?? "tamanpreet0007@gmail.com",
                PhoneNumber = farmer?.PhoneNumber ?? "+91 9896558903",
                Location = farmer?.Profile?.Location ?? "Phagwara, Punjab",
                FarmSize = farmer?.Profile?.FarmSize ?? 4.5,
                SoilType = farmer?.Profile?.SoilType ?? "Alluvial Loam",
                IrrigationType = farmer?.Profile?.IrrigationType ?? "Canal / Tube Well",
                PrimaryCrop = farmer?.Profile?.PrimaryCrop ?? "Wheat (Kanak) & Rice",
                Temperature = 24.5,
                WeatherCondition = "Sunny & Clear",
                Humidity = 58.0,
                WindSpeed = 11.2,
                WeatherTip = "Optimal morning conditions for field inspection. Ground moisture is favorable for Rabi crops.",
                LatestAdvisory = latestAdvisory,
                RecentMarketPrices = marketPrices,
                ActiveAlerts = new()
                {
                    new AlertItem { Title = "Yellow Rust Sentry Alert", Description = "Mild yellow rust spores spotted in neighbouring districts. Inspect wheat leaf undersides.", Severity = "Warning", TimeAgo = "2 hrs ago" },
                    new AlertItem { Title = "Mandi Price Gain: Basmati Paddy", Description = "Amritsar Mandi modal rate climbed +₹150/quintal over previous week.", Severity = "Normal", TimeAgo = "5 hrs ago" },
                    new AlertItem { Title = "Favorable Spray Window", Description = "Calm winds expected across Doaba region for the next 48 hours.", Severity = "Info", TimeAgo = "1 day ago" }
                }
            };

            return View(model);
        }

        [Authorize]
        [HttpGet]
        public async Task<IActionResult> Profile()
        {
            var farmerIdStr = User.FindFirstValue(ClaimTypes.NameIdentifier);
            Farmer? farmer = null;

            if (int.TryParse(farmerIdStr, out int fid))
            {
                farmer = await _context.Farmers
                    .Include(f => f.Profile)
                    .FirstOrDefaultAsync(f => f.Id == fid);
            }

            farmer ??= await _context.Farmers.Include(f => f.Profile).FirstOrDefaultAsync();
            var profile = farmer?.Profile ?? new FarmerProfile
            {
                Location = "Phagwara, Punjab",
                State = "Punjab",
                District = "Kapurthala",
                FarmSize = 4.5,
                SoilType = "Alluvial Loam",
                IrrigationType = "Canal / Tube Well",
                PrimaryCrop = "Wheat & Rice"
            };

            ViewBag.FarmerName = farmer?.FullName ?? "Taman Preet Singh";
            ViewBag.FarmerEmail = farmer?.Email ?? "farmer@agrisaarthi.in";
            ViewBag.FarmerPhone = farmer?.PhoneNumber ?? "+91 9896558903";

            return View(profile);
        }

        [Authorize]
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Profile(FarmerProfile model)
        {
            var farmerIdStr = User.FindFirstValue(ClaimTypes.NameIdentifier);
            if (int.TryParse(farmerIdStr, out int fid))
            {
                var existingProfile = await _context.FarmerProfiles.FirstOrDefaultAsync(p => p.FarmerId == fid);
                if (existingProfile == null)
                {
                    model.FarmerId = fid;
                    _context.FarmerProfiles.Add(model);
                }
                else
                {
                    existingProfile.Location = model.Location;
                    existingProfile.State = model.State;
                    existingProfile.District = model.District;
                    existingProfile.FarmSize = model.FarmSize;
                    existingProfile.SoilType = model.SoilType;
                    existingProfile.IrrigationType = model.IrrigationType;
                    existingProfile.PrimaryCrop = model.PrimaryCrop;
                    existingProfile.UpdatedAt = DateTime.UtcNow;
                }
                await _context.SaveChangesAsync();
                TempData["SuccessMessage"] = "Farmer profile updated successfully in SQL Server!";
            }

            return RedirectToAction(nameof(Profile));
        }
    }
}
