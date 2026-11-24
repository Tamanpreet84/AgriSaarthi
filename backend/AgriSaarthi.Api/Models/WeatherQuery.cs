using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AgriSaarthi.Api.Models
{
    public class WeatherQuery
    {
        [Key]
        public int Id { get; set; }

        public int FarmerId { get; set; }

        [ForeignKey("FarmerId")]
        public Farmer? Farmer { get; set; }

        [MaxLength(150)]
        public string City { get; set; } = string.Empty;

        public double Latitude { get; set; }
        public double Longitude { get; set; }

        public double Temperature { get; set; }
        public double Humidity { get; set; }
        public double WindSpeed { get; set; }

        [MaxLength(100)]
        public string Condition { get; set; } = string.Empty;

        public string AdvisoryNotes { get; set; } = string.Empty;

        public DateTime QueryDate { get; set; } = DateTime.UtcNow;
    }
}
