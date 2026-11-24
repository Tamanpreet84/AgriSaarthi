using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Threading.Tasks;
using AgriSaarthi.Api.DTOs;
using Microsoft.Extensions.Logging;

namespace AgriSaarthi.Api.Services
{
    public class MarketPriceService : IMarketPriceService
    {
        private readonly ILogger<MarketPriceService> _logger;
        private readonly JsonSerializerOptions _jsonOptions;

        public MarketPriceService(ILogger<MarketPriceService> logger)
        {
            _logger = logger;
            _jsonOptions = new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.CamelCase };
        }

        public async Task<List<MarketPriceDto>> GetMarketPricesAsync(string? crop = null, string? state = null)
        {
            try
            {
                var candidatePaths = new[]
                {
                    Path.Combine(Directory.GetCurrentDirectory(), "ml", "agri-knowledge", "market-prices.json"),
                    Path.Combine(Directory.GetCurrentDirectory(), "..", "ml", "agri-knowledge", "market-prices.json"),
                    Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "ml", "agri-knowledge", "market-prices.json"),
                    Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "..", "..", "..", "..", "ml", "agri-knowledge", "market-prices.json"),
                    @"C:\Users\taman\OneDrive\Desktop\agrisaarthi\ml\agri-knowledge\market-prices.json"
                };

                string? resolvedPath = candidatePaths.FirstOrDefault(File.Exists);

                List<MarketPriceDto> prices;

                if (resolvedPath != null)
                {
                    var json = await File.ReadAllTextAsync(resolvedPath);
                    prices = JsonSerializer.Deserialize<List<MarketPriceDto>>(json, _jsonOptions) ?? GetDefaultFallbackPrices();
                }
                else
                {
                    prices = GetDefaultFallbackPrices();
                }

                var query = prices.AsQueryable();

                if (!string.IsNullOrWhiteSpace(crop))
                {
                    query = query.Where(p => p.Crop.Contains(crop, StringComparison.OrdinalIgnoreCase));
                }

                if (!string.IsNullOrWhiteSpace(state))
                {
                    query = query.Where(p => p.State.Contains(state, StringComparison.OrdinalIgnoreCase));
                }

                return query.ToList();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error reading market prices");
                return GetDefaultFallbackPrices();
            }
        }

        private static List<MarketPriceDto> GetDefaultFallbackPrices()
        {
            return new List<MarketPriceDto>
            {
                new MarketPriceDto { Id = "mp_1", Crop = "Wheat", Market = "Khanna Mandi", State = "Punjab", Price = 2410, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_2", Crop = "Rice", Market = "Amritsar Mandi", State = "Punjab", Price = 4120, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_3", Crop = "Cotton", Market = "Bathinda Mandi", State = "Punjab", Price = 7250, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_4", Crop = "Mustard", Market = "Sirsa Mandi", State = "Haryana", Price = 5780, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_5", Crop = "Maize", Market = "Jalandhar Mandi", State = "Punjab", Price = 2150, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_6", Crop = "Potato", Market = "Hoshiarpur Mandi", State = "Punjab", Price = 1350, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow },
                new MarketPriceDto { Id = "mp_7", Crop = "Sugarcane", Market = "Phagwara Mandi", State = "Punjab", Price = 405, Unit = "Quintal", Source = "Agmarknet APMC", LastUpdated = DateTime.UtcNow }
            };
        }
    }
}
