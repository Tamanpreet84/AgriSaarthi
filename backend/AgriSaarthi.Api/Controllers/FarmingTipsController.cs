using System.Collections.Generic;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AgriSaarthi.Api.Controllers
{
    [Authorize]
    [Route("farming-tips")]
    public class FarmingTipsController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            var model = new FarmingTipsViewModel
            {
                CurrentSeason = "Rabi Season (November - April)",
                Tips = new List<TipItem>
                {
                    new TipItem
                    {
                        Title = "Crown Root Initiation (CRI) Irrigation for Wheat",
                        Category = "Water Management",
                        Content = "First irrigation must be applied strictly at 20-25 days after sowing (CRI stage). Delaying this single watering can permanently reduce tiller count by up to 20%.",
                        ActionBadge = "Crucial Stage"
                    },
                    new TipItem
                    {
                        Title = "Split Nitrogen Application Strategy",
                        Category = "Fertilizer Practice",
                        Content = "Never broadcast the entire Nitrogen dose at sowing. Apply 50% basal with DAP/MOP, 25% at first irrigation, and 25% at second irrigation before booting stage for maximum grain protein.",
                        ActionBadge = "High ROI"
                    },
                    new TipItem
                    {
                        Title = "Soil Moisture Testing Without Sensors",
                        Category = "Soil Health",
                        Content = "Take soil from 6-8 inches depth and squeeze it in your hand. If it forms a firm ball without leaving muddy water, moisture is adequate. If it crumbles, schedule irrigation.",
                        ActionBadge = "Practical Tip"
                    },
                    new TipItem
                    {
                        Title = "Integrated Pest Management (IPM) for Mustard Aphids",
                        Category = "Pest Control",
                        Content = "Install yellow sticky traps @ 10 traps per acre. Spray neem oil (1500 ppm) @ 5 ml/liter water at initial aphid clustering before economic threshold is breached.",
                        ActionBadge = "Eco-Friendly"
                    }
                }
            };

            return View(model);
        }
    }
}
