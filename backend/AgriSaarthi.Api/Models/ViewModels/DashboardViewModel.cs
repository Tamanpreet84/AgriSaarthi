using System;
using System.Collections.Generic;

namespace AgriSaarthi.Api.Models.ViewModels
{
    public class DashboardViewModel
    {
        public string FarmerName { get; set; } = "Farmer";
        public string Email { get; set; } = string.Empty;
        public string PhoneNumber { get; set; } = string.Empty;
        public string Location { get; set; } = "Punjab, India";
        public double FarmSize { get; set; } = 4.5;
        public string SoilType { get; set; } = "Alluvial Loam";
        public string IrrigationType { get; set; } = "Canal / Tube Well";
        public string PrimaryCrop { get; set; } = "Wheat & Rice";

        // Live Weather
        public double Temperature { get; set; } = 24.5;
        public string WeatherCondition { get; set; } = "Partly Cloudy";
        public double Humidity { get; set; } = 62;
        public double WindSpeed { get; set; } = 12.8;
        public string WeatherTip { get; set; } = "Optimal weather for crop field monitoring. Light irrigation recommended.";

        // Recent Crop Advisory
        public CropAdvisory? LatestAdvisory { get; set; }

        // Live Mandi Prices
        public List<MarketPriceItem> RecentMarketPrices { get; set; } = new();

        // System Alerts
        public List<AlertItem> ActiveAlerts { get; set; } = new();
    }

    public class AlertItem
    {
        public string Title { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public string Severity { get; set; } = "Normal"; // "Warning", "Normal", "Info"
        public string TimeAgo { get; set; } = "Just now";
    }
}
