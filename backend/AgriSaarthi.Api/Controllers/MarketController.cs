using System.Linq;
using System.Threading.Tasks;
using AgriSaarthi.Api.Data;
using AgriSaarthi.Api.Models.ViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AgriSaarthi.Api.Controllers
{
    [Authorize]
    [Route("market-prices")]
    public class MarketController : Controller
    {
        private readonly AgriSaarthiDbContext _context;

        public MarketController(AgriSaarthiDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<IActionResult> Index(string? state = "All", string? commodity = "All", string? search = "")
        {
            var query = _context.MarketPrices.AsQueryable();

            if (!string.IsNullOrEmpty(state) && state != "All")
            {
                query = query.Where(m => m.State == state);
            }

            if (!string.IsNullOrEmpty(commodity) && commodity != "All")
            {
                query = query.Where(m => m.Commodity.Contains(commodity));
            }

            if (!string.IsNullOrEmpty(search))
            {
                query = query.Where(m => m.Commodity.Contains(search) || m.Market.Contains(search));
            }

            var prices = await query.OrderBy(m => m.Commodity).ToListAsync();

            var model = new MarketPricesViewModel
            {
                SelectedState = state ?? "All",
                SelectedCommodity = commodity ?? "All",
                SearchTerm = search ?? "",
                Prices = prices
            };

            return View(model);
        }
    }
}
