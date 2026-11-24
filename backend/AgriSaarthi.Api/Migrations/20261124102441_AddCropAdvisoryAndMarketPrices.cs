using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

#pragma warning disable CA1814 // Prefer jagged arrays over multidimensional

namespace AgriSaarthi.Api.Migrations
{
    /// <inheritdoc />
    public partial class AddCropAdvisoryAndMarketPrices : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "CropAdvisories",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    FarmerId = table.Column<int>(type: "int", nullable: false),
                    Nitrogen = table.Column<double>(type: "float", nullable: false),
                    Phosphorus = table.Column<double>(type: "float", nullable: false),
                    Potassium = table.Column<double>(type: "float", nullable: false),
                    Temperature = table.Column<double>(type: "float", nullable: false),
                    Humidity = table.Column<double>(type: "float", nullable: false),
                    Ph = table.Column<double>(type: "float", nullable: false),
                    Rainfall = table.Column<double>(type: "float", nullable: false),
                    RecommendedCrop = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false),
                    ConfidenceScore = table.Column<double>(type: "float", nullable: false),
                    RequestDate = table.Column<DateTime>(type: "datetime2", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CropAdvisories", x => x.Id);
                    table.ForeignKey(
                        name: "FK_CropAdvisories_Farmers_FarmerId",
                        column: x => x.FarmerId,
                        principalTable: "Farmers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "MarketPrices",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Commodity = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false),
                    Market = table.Column<string>(type: "nvarchar(150)", maxLength: 150, nullable: false),
                    State = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false),
                    MinPrice = table.Column<decimal>(type: "decimal(18,2)", nullable: false),
                    MaxPrice = table.Column<decimal>(type: "decimal(18,2)", nullable: false),
                    ModalPrice = table.Column<decimal>(type: "decimal(18,2)", nullable: false),
                    Trend = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false),
                    UpdatedDate = table.Column<DateTime>(type: "datetime2", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_MarketPrices", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "WeatherQueries",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    FarmerId = table.Column<int>(type: "int", nullable: false),
                    City = table.Column<string>(type: "nvarchar(150)", maxLength: 150, nullable: false),
                    Latitude = table.Column<double>(type: "float", nullable: false),
                    Longitude = table.Column<double>(type: "float", nullable: false),
                    Temperature = table.Column<double>(type: "float", nullable: false),
                    Humidity = table.Column<double>(type: "float", nullable: false),
                    WindSpeed = table.Column<double>(type: "float", nullable: false),
                    Condition = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false),
                    AdvisoryNotes = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    QueryDate = table.Column<DateTime>(type: "datetime2", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_WeatherQueries", x => x.Id);
                    table.ForeignKey(
                        name: "FK_WeatherQueries_Farmers_FarmerId",
                        column: x => x.FarmerId,
                        principalTable: "Farmers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.InsertData(
                table: "MarketPrices",
                columns: new[] { "Id", "Commodity", "Market", "MaxPrice", "MinPrice", "ModalPrice", "State", "Trend", "UpdatedDate" },
                values: new object[,]
                {
                    { 1, "Wheat (Kanak)", "Khanna Mandi", 2450m, 2275m, 2375m, "Punjab", "up", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 2, "Paddy (Basmati)", "Amritsar Mandi", 4250m, 3600m, 3950m, "Punjab", "up", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 3, "Cotton (Kapas)", "Bathinda Mandi", 7450m, 6900m, 7200m, "Punjab", "down", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 4, "Maize (Makka)", "Jalandhar Mandi", 2200m, 1950m, 2100m, "Punjab", "stable", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 5, "Mustard (Sarson)", "Sirsa Mandi", 5850m, 5400m, 5650m, "Haryana", "up", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 6, "Potato (Aloo)", "Hoshiarpur Mandi", 1450m, 1100m, 1300m, "Punjab", "up", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) },
                    { 7, "Sugarcane", "Phagwara Mandi", 410m, 380m, 395m, "Punjab", "stable", new DateTime(2026, 11, 20, 0, 0, 0, 0, DateTimeKind.Unspecified) }
                });

            migrationBuilder.CreateIndex(
                name: "IX_CropAdvisories_FarmerId",
                table: "CropAdvisories",
                column: "FarmerId");

            migrationBuilder.CreateIndex(
                name: "IX_WeatherQueries_FarmerId",
                table: "WeatherQueries",
                column: "FarmerId");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "CropAdvisories");

            migrationBuilder.DropTable(
                name: "MarketPrices");

            migrationBuilder.DropTable(
                name: "WeatherQueries");
        }
    }
}
