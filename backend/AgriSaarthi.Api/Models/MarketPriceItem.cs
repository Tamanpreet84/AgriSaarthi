using System;
using System.ComponentModel.DataAnnotations;

namespace AgriSaarthi.Api.Models
{
    public class MarketPriceItem
    {
        [Key]
        public int Id { get; set; }

        [Required]
        [MaxLength(100)]
        public string Commodity { get; set; } = string.Empty;

        [Required]
        [MaxLength(150)]
        public string Market { get; set; } = string.Empty;

        [Required]
        [MaxLength(100)]
        public string State { get; set; } = string.Empty;

        public decimal MinPrice { get; set; }
        public decimal MaxPrice { get; set; }
        public decimal ModalPrice { get; set; }

        [MaxLength(20)]
        public string Trend { get; set; } = "up"; // "up", "down", "stable"

        public DateTime UpdatedDate { get; set; } = DateTime.UtcNow;
    }
}
