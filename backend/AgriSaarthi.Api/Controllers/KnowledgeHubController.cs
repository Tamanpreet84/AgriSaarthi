using System.Collections.Generic;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AgriSaarthi.Api.Controllers
{
    [Authorize]
    [Route("knowledge-hub")]
    public class KnowledgeHubController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            var model = new KnowledgeHubViewModel
            {
                CropGuides = new List<CropGuideItem>
                {
                    new CropGuideItem
                    {
                        CropName = "Wheat (Triticum aestivum)",
                        Season = "Rabi (Winter)",
                        IdealSoil = "Well-drained fertile loam / clay loam (pH 6.0 - 7.5)",
                        WaterNeed = "450 - 650 mm (4 to 6 irrigations)",
                        ExpectedYield = "20 - 24 Quintals / Acre",
                        Description = "The staple cereal crop of North-Western India. Optimal sowing temperature is 18-22°C. Varieties like HD-3086, DBW-187, and PBW-824 show high disease tolerance."
                    },
                    new CropGuideItem
                    {
                        CropName = "Basmati Rice (Oryza sativa)",
                        Season = "Kharif (Monsoon)",
                        IdealSoil = "Heavy clay or clay-loam with high water retention (pH 5.5 - 7.0)",
                        WaterNeed = "1200 - 1500 mm (Standing water recommended)",
                        ExpectedYield = "18 - 22 Quintals / Acre",
                        Description = "Aromatic long-grain rice fetching premium export prices. Varieties like Pusa 1121 and Pusa 1718 require precise nursery transplantation and balanced Zinc."
                    },
                    new CropGuideItem
                    {
                        CropName = "Mustard / Rapeseed (Brassica juncea)",
                        Season = "Rabi (Winter)",
                        IdealSoil = "Sandy loam to clay loam (pH 6.0 - 8.0)",
                        WaterNeed = "250 - 400 mm (Drought-tolerant, 2-3 irrigations)",
                        ExpectedYield = "8 - 10 Quintals / Acre",
                        Description = "Major oilseed crop in northern drylands. Highly sensitive to frost at pod development. Sulfur application significantly increases oil content."
                    }
                },
                GovernmentSchemes = new List<SchemeItem>
                {
                    new SchemeItem
                    {
                        Name = "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
                        Benefit = "₹6,000 per year directly transferred to bank accounts in 3 equal installments of ₹2,000.",
                        Eligibility = "All landholding farmer families with cultivable land in their names.",
                        OfficialPortal = "pmkisan.gov.in"
                    },
                    new SchemeItem
                    {
                        Name = "PMFBY (Pradhan Mantri Fasal Bima Yojana)",
                        Benefit = "Comprehensive crop insurance covering non-preventable natural risks (drought, flood, pests) at nominal farmer premiums (1.5% Rabi, 2% Kharif).",
                        Eligibility = "All farmers growing notified crops in notified areas.",
                        OfficialPortal = "pmfby.gov.in"
                    },
                    new SchemeItem
                    {
                        Name = "Soil Health Card Scheme",
                        Benefit = "Free periodic soil chemical testing providing customized N-P-K and micronutrient dosage cards.",
                        Eligibility = "All operational agricultural landholders across India.",
                        OfficialPortal = "soilhealth.dac.gov.in"
                    }
                }
            };

            return View(model);
        }
    }
}
