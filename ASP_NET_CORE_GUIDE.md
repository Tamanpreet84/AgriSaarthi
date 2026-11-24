
# AgriSaarthi: ASP.NET Core & Microsoft SQL Server Architecture Guide

## Overview
AgriSaarthi is an enterprise smart agriculture platform developed using **ASP.NET Core 10**, **C#**, and **Microsoft SQL Server (LocalDB)**. The entire web interface, business logic, authentication, and database persistence are implemented in **C#** and **ASP.NET Core MVC with Razor Views**.

---

## 1. Visual Studio Solution Structure
Open `AgriSaarthi.sln` directly in **Microsoft Visual Studio 2022 / 2025 Community**:

```
AgriSaarthi.sln
└── AgriSaarthi.Api (ASP.NET Core 10 Web App)
    ├── Controllers/                       <- C# MVC & API Controllers
    │   ├── HomeController.cs              <- Dashboard & Farmer Profile actions
    │   ├── AccountController.cs           <- Farmer Registration, Login, Logout (Cookies + Hashing)
    │   ├── CropController.cs              <- Crop Recommendation (7-Factor ML + Fallback Engine)
    │   ├── WeatherViewController.cs       <- 7-Day Hyperlocal Weather Advisory
    │   ├── MarketController.cs            <- Mandi Market Rates Tracker
    │   ├── DiseaseController.cs           <- Plant Health & Disease Pathology Scanner
    │   ├── FarmingTipsController.cs       <- Seasonal Agronomic Best Practices
    │   ├── KnowledgeHubController.cs      <- Crop Production Manuals & Government Schemes
    │   └── AuthController.cs              <- REST API JWT Endpoints
    │
    ├── Models/                            <- C# Entity & ViewModel Classes
    │   ├── Farmer.cs                      <- Farmer Account Entity (SQL Server Table: Farmers)
    │   ├── FarmerProfile.cs               <- Farm Specs (SQL Server Table: FarmerProfiles)
    │   ├── CropAdvisory.cs                <- ML Advisory Logs (SQL Server Table: CropAdvisories)
    │   ├── WeatherQuery.cs                <- Weather Logs (SQL Server Table: WeatherQueries)
    │   ├── MarketPriceItem.cs             <- Mandi Prices (SQL Server Table: MarketPrices)
    │   └── ViewModels/
    │       ├── AuthViewModels.cs          <- LoginViewModel & RegisterViewModel
    │       ├── DashboardViewModel.cs      <- Metrics, Weather, Alerts & Profile
    │       ├── CropRecommendationViewModel.cs <- 7 Input Parameters & Results
    │       └── AdditionalViewModels.cs    <- Weather, Market, Disease & Knowledge ViewModels
    │
    ├── Views/                             <- ASP.NET Core Razor Views (.cshtml)
    │   ├── _ViewImports.cshtml            <- TagHelpers and Model imports
    │   ├── _ViewStart.cshtml              <- Master Layout assignment
    │   ├── Shared/
    │   │   └── _Layout.cshtml             <- Master Responsive Layout (Sidebar, Navbar, Mobile Bar)
    │   ├── Home/
    │   │   ├── Dashboard.cshtml           <- Main Farmer Dashboard (Cards, Weather, Mandi, Alerts)
    │   │   └── Profile.cshtml             <- Farmer Profile & Farm Settings Editor
    │   ├── Account/
    │   │   ├── Login.cshtml               <- Farmer Sign-In Page
    │   │   └── Register.cshtml            <- Farmer Account Registration Page
    │   ├── Crop/
    │   │   └── Recommend.cshtml           <- 7-Factor Soil/Climate Crop Recommendation Form
    │   ├── WeatherView/
    │   │   └── Index.cshtml               <- 7-Day Weather Forecast & Farming Guidelines
    │   ├── Market/
    │   │   └── Index.cshtml               <- Live Mandi Rates Table with Filtering
    │   ├── Disease/
    │   │   └── Index.cshtml               <- Plant Leaf Pathology Diagnosis & Treatment
    │   ├── FarmingTips/
    │   │   └── Index.cshtml               <- Seasonal Advisory & Irrigation Schedules
    │   └── KnowledgeHub/
    │       └── Index.cshtml               <- Crop Manuals & Government Schemes
    │
    ├── Data/
    │   ├── AgriSaarthiDbContext.cs        <- Entity Framework Core SQL Server DbContext
    │   └── Migrations/                    <- Code-First SQL Server Migrations
    │
    ├── Services/                          <- C# Business Logic & External Service Clients
    │   ├── AuthService.cs                 <- BCrypt Password Hashing & JWT Generation
    │   ├── FarmerService.cs               <- Farmer Profile Querying & Mutation
    │   ├── AiService.cs                   <- HTTP Client to FastAPI Microservice
    │   └── WeatherService.cs              <- HTTP Client to Open-Meteo REST API
    │
    ├── Program.cs                         <- Application Entry Point, DI, Auth & Middleware
    └── appsettings.json                   <- SQL Server Connection String & Settings
```

---

## 2. Microsoft SQL Server Database Configuration
The application automatically binds to Microsoft SQL Server LocalDB via Entity Framework Core:

```json
"ConnectionStrings": {
  "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=AgriSaarthiDb;Trusted_Connection=True;MultipleActiveResultSets=true;TrustServerCertificate=True"
}
```

### Relational Schema (Tables in `AgriSaarthiDb`):
1. **`Farmers`**: Stores primary farmer accounts (`Id`, `FullName`, `Email` [Unique Index], `PhoneNumber` [Unique Index], `PasswordHash`, `CreatedAt`).
2. **`FarmerProfiles`**: One-to-one foreign key with `Farmers` (`FarmerId`, `Location`, `State`, `District`, `FarmSize`, `SoilType`, `IrrigationType`, `PrimaryCrop`).
3. **`CropAdvisories`**: Stores historical crop predictions (`FarmerId`, `Nitrogen`, `Phosphorus`, `Potassium`, `Temperature`, `Humidity`, `Ph`, `Rainfall`, `RecommendedCrop`, `ConfidenceScore`, `RequestDate`).
4. **`WeatherQueries`**: Stores historical weather advisory inquiries (`FarmerId`, `City`, `Latitude`, `Longitude`, `Temperature`, `Humidity`, `WindSpeed`, `Condition`, `AdvisoryNotes`).
5. **`MarketPrices`**: Stores daily Mandi commodity prices (`Commodity`, `Market`, `State`, `MinPrice`, `MaxPrice`, `ModalPrice`, `Trend`, `UpdatedDate`).

---

## 3. How to Run in Microsoft Visual Studio (For Presentation)
1. Double-click `AgriSaarthi.sln` to open the project in **Microsoft Visual Studio**.
2. In the top toolbar, verify the launch profile dropdown is set to **`http`** (or `AgriSaarthi.Api`).
3. Press **`F5`** (or click the green **Play ▶** button).
4. Visual Studio will:
   - Build the C# solution (0 errors).
   - Boot up Kestrel on `http://localhost:5000`.
   - Connect to Microsoft SQL Server LocalDB and verify EF Core migrations.
   - Automatically launch your default browser to `http://localhost:5000/Account/Login`!

---

## 4. Key Highlights to Demonstrate to Faculty / Supervisor
- **Pure C# & ASP.NET Core**: All Controllers (`Controllers/`), ViewModels (`Models/ViewModels/`), and Razor Views (`Views/`) are written in standard C# and ASP.NET Core MVC.
- **Relational Integrity**: Show `AgriSaarthiDbContext.cs` and the SQL Server LocalDB tables with EF Core Migrations.
- **Security & Authentication**: Salted password hashing with BCrypt + Cookie session authentication + Anti-Forgery Token protection (`@Html.AntiForgeryToken()`).
- **Resilient AI Pipeline**: Crop recommendation queries the Python FastAPI AI service, and includes a fallback C# agronomic inference engine if the microservice is offline.
