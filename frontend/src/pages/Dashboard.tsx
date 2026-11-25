import { CloudSun, IndianRupee, Beaker } from 'lucide-react';
import { WelcomeSection, SummaryCard } from '../components/dashboard/DashboardCore';
import {
  FarmOverviewCard, WeatherCard, DiseaseDetectionCard,
  CropRecommendationSummaryCard, MarketPricesTableCard,
  PestDiseaseAlertsCard
} from '../components/dashboard/DashboardWidgets';
import { ExtrasRow } from '../components/dashboard/DashboardExtras';
import { useAppSettings } from '../context/AppSettingsContext';

export default function Dashboard() {
  const { t } = useAppSettings();

  return (
    <div className="max-w-[1400px] mx-auto space-y-4 md:space-y-6">
      {/* Top Welcome */}
      <WelcomeSection />

      {/* 4 Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <SummaryCard
          title={t('card_crop_title')}
          value={t('card_crop_val')}
          subtitle={t('card_crop_sub')}
          icon={<LeafIcon className="w-5 h-5" />}
          colorClass="bg-emerald-100 text-[#27ae60]"
          to="/crop-recommendation"
        />
        <SummaryCard
          title={t('card_weather_title')}
          value={t('card_weather_val')}
          subtitle={t('card_weather_sub')}
          icon={<CloudSun size={20} />}
          colorClass="bg-sky-100 text-sky-500"
          to="/weather"
        />
        <SummaryCard
          title={t('card_market_title')}
          value={t('card_market_val')}
          subtitle={t('card_market_sub')}
          icon={<IndianRupee size={20} />}
          colorClass="bg-amber-100 text-amber-600"
          to="/market-prices"
        />
        <SummaryCard
          title={t('card_disease_title')}
          value={t('card_disease_val')}
          subtitle={t('card_disease_sub')}
          icon={<Beaker size={20} />}
          colorClass="bg-[#e8f3ee] text-[#145a32]"
          to="/disease-detection"
        />
      </div>

      {/* Main Grid Area */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 lg:gap-6">
        {/* Left Column */}
        <div className="lg:col-span-2 space-y-4 lg:space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 h-auto">
            <FarmOverviewCard />
            <CropRecommendationSummaryCard />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 h-auto">
            <DiseaseDetectionCard />
            <PestDiseaseAlertsCard />
          </div>
        </div>

        {/* Right Column */}
        <div className="space-y-4 lg:space-y-6 flex flex-col">
          <div className="h-auto">
            <WeatherCard />
          </div>
          <div className="flex-1 min-h-[250px]">
            <MarketPricesTableCard />
          </div>
        </div>
      </div>

      {/* Bottom Banners */}
      <ExtrasRow />
    </div>
  );
}

function LeafIcon(props: any) {
  return <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>;
}
