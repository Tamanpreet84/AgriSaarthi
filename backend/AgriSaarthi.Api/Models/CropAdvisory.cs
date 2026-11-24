using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AgriSaarthi.Api.Models
{
    public class CropAdvisory
    {
        [Key]
        public int Id { get; set; }

        public int FarmerId { get; set; }

        [ForeignKey("FarmerId")]
        public Farmer? Farmer { get; set; }

        [Required]
        public double Nitrogen { get; set; }

        [Required]
        public double Phosphorus { get; set; }

        [Required]
        public double Potassium { get; set; }

        [Required]
        public double Temperature { get; set; }

        [Required]
        public double Humidity { get; set; }

        [Required]
        public double Ph { get; set; }

        [Required]
        public double Rainfall { get; set; }

        [Required]
        [MaxLength(100)]
        public string RecommendedCrop { get; set; } = string.Empty;

        public double ConfidenceScore { get; set; }

        public DateTime RequestDate { get; set; } = DateTime.UtcNow;
    }
}
