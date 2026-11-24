using System;
using System.Collections.Generic;

namespace AgriSaarthi.Api.Models.ViewModels
{
    public class WeatherViewModel
    {
        public string City { get; set; } = "Phagwara, Punjab";
        public double Latitude { get; set; } = 31.2240;
        public double Longitude { get; set; } = 75.7708;
        public double CurrentTemp { get; set; } = 24.5;
        public string Condition { get; set; } = "Partly Cloudy";
        public double Humidity { get; set; } = 62.0;
        public double WindSpeed { get; set; } = 12.8;
        public double RainfallProbability { get; set; } = 15.0;
        public string SowingStatus { get; set; } = "Favorable for Field Preparation";
        public string IrrigationAdvice { get; set; } = "Normal irrigation required. No heavy rain expected in 48 hours.";
        public string SprayingAdvice { get; set; } = "Wind speed is calm (12 km/h). Safe for foliar spray before 11:00 AM.";
        public List<DailyForecastItem> Forecast { get; set; } = new();
    }

    public class DailyForecastItem
    {
        public string Day { get; set; } = string.Empty;
        public string Date { get; set; } = string.Empty;
        public double TempMax { get; set; }
        public double TempMin { get; set; }
        public string Condition { get; set; } = string.Empty;
        public double RainChance { get; set; }
    }

    public class MarketPricesViewModel
    {
        public string SelectedState { get; set; } = "All";
        public string SelectedCommodity { get; set; } = "All";
        public string SearchTerm { get; set; } = string.Empty;
        public List<MarketPriceItem> Prices { get; set; } = new();
    }

    public class DiseaseDetectionViewModel
    {
        public string SelectedCrop { get; set; } = "Wheat";
        public bool HasDiagnosis { get; set; } = false;
        public string DiseaseName { get; set; } = string.Empty;
        public double ConfidencePercent { get; set; }
        public string Severity { get; set; } = "Moderate";
        public string Description { get; set; } = string.Empty;
        public string? UploadedImageBase64 { get; set; }
        public string? ImageFileName { get; set; }
        public string? ErrorMessage { get; set; }
        public List<string> Symptoms { get; set; } = new();
        public List<string> RecommendedTreatments { get; set; } = new();
        public List<string> PreventiveMeasures { get; set; } = new();
    }

    public class FarmingTipsViewModel
    {
        public string CurrentSeason { get; set; } = "Rabi Season (Winter Sowing)";
        public List<TipItem> Tips { get; set; } = new();
    }

    public class TipItem
    {
        public string Title { get; set; } = string.Empty;
        public string Category { get; set; } = "Soil & Fertilizer"; // "Water", "Pest", "Crop Management"
        public string Content { get; set; } = string.Empty;
        public string ActionBadge { get; set; } = "High Impact";
    }

    public class KnowledgeHubViewModel
    {
        public List<CropGuideItem> CropGuides { get; set; } = new();
        public List<SchemeItem> GovernmentSchemes { get; set; } = new();
    }

    public class CropGuideItem
    {
        public string CropName { get; set; } = string.Empty;
        public string Season { get; set; } = string.Empty;
        public string IdealSoil { get; set; } = string.Empty;
        public string WaterNeed { get; set; } = string.Empty;
        public string ExpectedYield { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
    }

    public class SchemeItem
    {
        public string Name { get; set; } = string.Empty;
        public string Benefit { get; set; } = string.Empty;
        public string Eligibility { get; set; } = string.Empty;
        public string OfficialPortal { get; set; } = string.Empty;
    }
}
