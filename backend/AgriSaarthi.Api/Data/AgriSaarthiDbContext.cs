using System;
using AgriSaarthi.Api.Models;
using Microsoft.EntityFrameworkCore;

namespace AgriSaarthi.Api.Data
{
    public class AgriSaarthiDbContext : DbContext
    {
        public AgriSaarthiDbContext(DbContextOptions<AgriSaarthiDbContext> options) : base(options)
        {
        }

        public DbSet<Farmer> Farmers { get; set; } = null!;
        public DbSet<FarmerProfile> FarmerProfiles { get; set; } = null!;
        public DbSet<CropAdvisory> CropAdvisories { get; set; } = null!;
        public DbSet<WeatherQuery> WeatherQueries { get; set; } = null!;
        public DbSet<MarketPriceItem> MarketPrices { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure One-to-One relationship
            modelBuilder.Entity<Farmer>()
                .HasOne(f => f.Profile)
                .WithOne(p => p.Farmer)
                .HasForeignKey<FarmerProfile>(p => p.FarmerId)
                .OnDelete(DeleteBehavior.Cascade);
            
            // Ensure unique email and phone
            modelBuilder.Entity<Farmer>()
                .HasIndex(f => f.Email)
                .IsUnique();
                
            modelBuilder.Entity<Farmer>()
                .HasIndex(f => f.PhoneNumber)
                .IsUnique();

            // Seed initial Mandi Market Prices
            modelBuilder.Entity<MarketPriceItem>().HasData(
                new MarketPriceItem { Id = 1, Commodity = "Wheat (Kanak)", Market = "Khanna Mandi", State = "Punjab", MinPrice = 2275, MaxPrice = 2450, ModalPrice = 2375, Trend = "up", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 2, Commodity = "Paddy (Basmati)", Market = "Amritsar Mandi", State = "Punjab", MinPrice = 3600, MaxPrice = 4250, ModalPrice = 3950, Trend = "up", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 3, Commodity = "Cotton (Kapas)", Market = "Bathinda Mandi", State = "Punjab", MinPrice = 6900, MaxPrice = 7450, ModalPrice = 7200, Trend = "down", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 4, Commodity = "Maize (Makka)", Market = "Jalandhar Mandi", State = "Punjab", MinPrice = 1950, MaxPrice = 2200, ModalPrice = 2100, Trend = "stable", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 5, Commodity = "Mustard (Sarson)", Market = "Sirsa Mandi", State = "Haryana", MinPrice = 5400, MaxPrice = 5850, ModalPrice = 5650, Trend = "up", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 6, Commodity = "Potato (Aloo)", Market = "Hoshiarpur Mandi", State = "Punjab", MinPrice = 1100, MaxPrice = 1450, ModalPrice = 1300, Trend = "up", UpdatedDate = new DateTime(2026, 11, 20) },
                new MarketPriceItem { Id = 7, Commodity = "Sugarcane", Market = "Phagwara Mandi", State = "Punjab", MinPrice = 380, MaxPrice = 410, ModalPrice = 395, Trend = "stable", UpdatedDate = new DateTime(2026, 11, 20) }
            );
        }
    }
}
