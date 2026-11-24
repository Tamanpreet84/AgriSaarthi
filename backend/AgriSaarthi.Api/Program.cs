using System.Text;
using AgriSaarthi.Api.Data;
using AgriSaarthi.Api.Services;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;

var builder = WebApplication.CreateBuilder(args);

// Add MVC Controllers with Razor Views and API Explorer
builder.Services.AddControllersWithViews();
builder.Services.AddEndpointsApiExplorer();

// Database Configuration (Microsoft SQL Server LocalDB)
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") 
    ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
builder.Services.AddDbContext<AgriSaarthiDbContext>(options =>
    options.UseSqlServer(connectionString));

// Application Services
builder.Services.AddScoped<IFarmerService, FarmerService>();
builder.Services.AddScoped<IAuthService, AuthService>();
builder.Services.AddScoped<IAgriKnowledgeService, AgriKnowledgeService>();
builder.Services.AddScoped<IMarketPriceService, MarketPriceService>();
builder.Services.AddScoped<IFarmingTipsService, FarmingTipsService>();
builder.Services.AddHttpClient<IAiService, AiService>();
builder.Services.AddHttpClient<IWeatherService, WeatherService>();

// Dual Authentication Configuration: Cookies for Web UI, JWT Bearer for REST APIs
var jwtKey = builder.Configuration["Jwt:Key"] ?? "A_Super_Secret_Key_For_AgriSaarthi_Development_Do_Not_Use_In_Prod";

builder.Services.AddAuthentication(options =>
{
    options.DefaultScheme = "JWT_OR_COOKIE";
    options.DefaultChallengeScheme = "JWT_OR_COOKIE";
})
.AddPolicyScheme("JWT_OR_COOKIE", "JWT_OR_COOKIE", options =>
{
    options.ForwardDefaultSelector = context =>
    {
        var authHeader = context.Request.Headers["Authorization"].FirstOrDefault();
        if (!string.IsNullOrEmpty(authHeader) && authHeader.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase))
        {
            return JwtBearerDefaults.AuthenticationScheme;
        }
        if (context.Request.Path.StartsWithSegments("/api"))
        {
            return JwtBearerDefaults.AuthenticationScheme;
        }
        return CookieAuthenticationDefaults.AuthenticationScheme;
    };
})
.AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options =>
{
    options.LoginPath = "/Account/Login";
    options.LogoutPath = "/Account/Logout";
    options.AccessDeniedPath = "/Account/Login";
    options.ExpireTimeSpan = TimeSpan.FromDays(7);
    options.SlidingExpiration = true;
    options.Cookie.Name = "AgriSaarthi.Auth";
    options.Events.OnRedirectToLogin = context =>
    {
        if (context.Request.Path.StartsWithSegments("/api"))
        {
            context.Response.StatusCode = StatusCodes.Status401Unauthorized;
            return Task.CompletedTask;
        }
        context.Response.Redirect(context.RedirectUri);
        return Task.CompletedTask;
    };
})
.AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,
        ValidIssuer = builder.Configuration["Jwt:Issuer"] ?? "AgriSaarthiApi",
        ValidAudience = builder.Configuration["Jwt:Audience"] ?? "AgriSaarthiFrontend",
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtKey))
    };
});

// Configure CORS
var frontendUrls = builder.Configuration.GetSection("Cors:AllowedOrigins").Get<string[]>() 
                   ?? new[] { builder.Configuration["FrontendUrl"] ?? "http://localhost:5173", "http://localhost:5000" };

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowFrontend",
        policy => policy.WithOrigins(frontendUrls)
                        .AllowAnyMethod()
                        .AllowAnyHeader()
                        .AllowCredentials());
});

var app = builder.Build();

// Static Files & Web Assets
app.UseStaticFiles();

app.UseRouting();

app.UseCors("AllowFrontend");

app.UseAuthentication();
app.UseAuthorization();

// MVC Route Pattern
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

// Web API Controllers (/api/...)
app.MapControllers();

// Automated EF Core Migrations and Seed Verification on Startup
using (var scope = app.Services.CreateScope())
{
    var dbContext = scope.ServiceProvider.GetRequiredService<AgriSaarthiDbContext>();
    dbContext.Database.Migrate();
}

app.Run();
