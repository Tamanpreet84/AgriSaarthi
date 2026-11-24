using System.ComponentModel.DataAnnotations;

namespace AgriSaarthi.Api.Models.ViewModels
{
    public class CropRecommendationViewModel
    {
        [Required(ErrorMessage = "Nitrogen ratio is required.")]
        [Range(0, 200, ErrorMessage = "Nitrogen must be between 0 and 200.")]
        [Display(Name = "Nitrogen (N) - mg/kg")]
        public double Nitrogen { get; set; } = 90.0;

        [Required(ErrorMessage = "Phosphorus ratio is required.")]
        [Range(0, 200, ErrorMessage = "Phosphorus must be between 0 and 200.")]
        [Display(Name = "Phosphorus (P) - mg/kg")]
        public double Phosphorus { get; set; } = 42.0;

        [Required(ErrorMessage = "Potassium ratio is required.")]
        [Range(0, 300, ErrorMessage = "Potassium must be between 0 and 300.")]
        [Display(Name = "Potassium (K) - mg/kg")]
        public double Potassium { get; set; } = 43.0;

        [Required(ErrorMessage = "Temperature is required.")]
        [Range(5, 50, ErrorMessage = "Temperature must be between 5°C and 50°C.")]
        [Display(Name = "Temperature (°C)")]
        public double Temperature { get; set; } = 25.5;

        [Required(ErrorMessage = "Humidity is required.")]
        [Range(10, 100, ErrorMessage = "Humidity must be between 10% and 100%.")]
        [Display(Name = "Relative Humidity (%)")]
        public double Humidity { get; set; } = 82.0;

        [Required(ErrorMessage = "Soil pH is required.")]
        [Range(3.0, 10.0, ErrorMessage = "pH must be between 3.0 and 10.0.")]
        [Display(Name = "Soil pH Level (0-14)")]
        public double Ph { get; set; } = 6.5;

        [Required(ErrorMessage = "Rainfall is required.")]
        [Range(10, 500, ErrorMessage = "Rainfall must be between 10mm and 500mm.")]
        [Display(Name = "Annual Rainfall (mm)")]
        public double Rainfall { get; set; } = 202.0;

        // Results
        public bool HasResult { get; set; } = false;
        public string RecommendedCrop { get; set; } = string.Empty;
        public double ConfidenceScore { get; set; } = 0.0;
        public int ConfidencePercent => (int)(ConfidenceScore * 100);
        public string SuitabilityNotes { get; set; } = string.Empty;
        public string FertilizerAdvice { get; set; } = string.Empty;
        public string SowingSeason { get; set; } = string.Empty;
        public string WaterRequirement { get; set; } = string.Empty;
        public string Message { get; set; } = string.Empty;
    }
}
