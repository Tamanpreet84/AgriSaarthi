using System;
using System.Collections.Generic;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AgriSaarthi.Api.Controllers
{
    [Authorize]
    [Route("weather")]
    public class WeatherViewController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            var model = new WeatherViewModel
            {
                City = "Phagwara, Punjab",
                Latitude = 31.2240,
                Longitude = 75.7708,
                CurrentTemp = 24.5,
                Condition = "Partly Cloudy",
                Humidity = 62.0,
                WindSpeed = 12.8,
                RainfallProbability = 15.0,
                SowingStatus = "Highly Favorable for Rabi Crop Monitoring",
                IrrigationAdvice = "Soil moisture is currently stable. Delay next irrigation by 2 days to prevent root rot.",
                SprayingAdvice = "Calm morning winds (10-12 km/h). Optimal spraying window between 8:00 AM and 11:30 AM.",
                Forecast = new List<DailyForecastItem>
                {
                    new DailyForecastItem { Day = "Today", Date = "Nov 24", TempMax = 26.0, TempMin = 14.5, Condition = "Partly Cloudy", RainChance = 10 },
                    new DailyForecastItem { Day = "Tomorrow", Date = "Nov 25", TempMax = 25.5, TempMin = 13.8, Condition = "Sunny", RainChance = 5 },
                    new DailyForecastItem { Day = "Wednesday", Date = "Nov 26", TempMax = 24.8, TempMin = 13.0, Condition = "Clear Sky", RainChance = 0 },
                    new DailyForecastItem { Day = "Thursday", Date = "Nov 27", TempMax = 23.5, TempMin = 12.5, Condition = "Clear Sky", RainChance = 0 },
                    new DailyForecastItem { Day = "Friday", Date = "Nov 28", TempMax = 24.0, TempMin = 13.2, Condition = "Mild Foggy Morning", RainChance = 10 },
                    new DailyForecastItem { Day = "Saturday", Date = "Nov 29", TempMax = 25.0, TempMin = 14.0, Condition = "Sunny", RainChance = 15 },
                    new DailyForecastItem { Day = "Sunday", Date = "Nov 30", TempMax = 23.8, TempMin = 13.5, Condition = "Light Cloud Cover", RainChance = 20 }
                }
            };

            return View(model);
        }
    }
}
