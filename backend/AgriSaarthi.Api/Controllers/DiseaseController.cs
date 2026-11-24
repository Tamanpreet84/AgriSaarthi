using System.Collections.Generic;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AgriSaarthi.Api.Controllers
{
    [Authorize]
    [Route("disease-detection")]
    public class DiseaseController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            var model = new DiseaseDetectionViewModel
            {
                SelectedCrop = "Wheat",
                HasDiagnosis = true,
                DiseaseName = "Yellow Rust (Stripe Rust) — Puccinia striiformis",
                ConfidencePercent = 96.4,
                Severity = "Moderate Early Stage",
                Description = "A major fungal foliar disease characterized by bright yellowish-orange pustules arranged in linear stripes along wheat leaf blades.",
                Symptoms = new List<string>
                {
                    "Narrow, parallel yellowish chlorotic stripes on mature leaf surfaces.",
                    "Powdery yellow pustules (urediniospores) that rub off on fingertips.",
                    "Premature leaf drying leading to shriveled grains and 20-30% yield penalty if untreated."
                },
                RecommendedTreatments = new List<string>
                {
                    "Apply Propiconazole 25% EC @ 200 ml in 200 liters of water per acre immediately upon sighting.",
                    "Alternative: Tebuconazole 25.9% EC @ 200 ml/acre or Azoxystrobin + Difenoconazole @ 200 ml/acre.",
                    "Spray during morning hours when leaf dew has dried."
                },
                PreventiveMeasures = new List<string>
                {
                    "Cultivate recommended rust-resistant varieties (e.g. PBW-824, DBW-187, DBW-303).",
                    "Avoid excessive Nitrogen top-dressing which makes leaves tender and disease-prone.",
                    "Maintain optimal plant spacing to allow adequate aeration."
                }
            };

            return View(model);
        }
    }
}
