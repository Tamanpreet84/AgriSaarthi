import React, { createContext, useContext, useEffect, useState } from 'react';

export type Language = 'en' | 'hi' | 'pa';
export type Theme = 'light' | 'dark';

const translations: Record<Language, Record<string, string>> = {
  en: {
    brand_tag: "AI-Powered Crop Advisory & Farmer's Companion",
    know_more: "KNOW MORE GROW MORE",
    nav_dashboard: "Dashboard",
    nav_profile: "Farmer Profile",
    nav_crop: "Crop Recommendation",
    nav_disease: "Disease Detection",
    nav_weather: "Weather Advisory",
    nav_pest: "Pest & Disease Info",
    nav_market: "Market Prices",
    nav_tips: "Farming Tips",
    nav_knowledge: "Knowledge Hub",
    nav_settings: "Settings",
    logout: "Logout",
    need_advice: "Need Advice?",
    explore_resources: "Explore our resources",
    farmer_role: "Registered Farmer",
    greeting_morning: "Good Morning",
    greeting_afternoon: "Good Afternoon",
    greeting_evening: "Good Evening",
    welcome_quote: "\"Better Information. Healthier Crops. A Prosperous Tomorrow.\"",
    card_crop_title: "Crop Recommendation",
    card_crop_val: "Find Best Crop",
    card_crop_sub: "Based on soil & climate",
    card_weather_title: "Weather Forecast",
    card_weather_val: "Check Advisory",
    card_weather_sub: "Localized farm weather",
    card_market_title: "Reference Prices",
    card_market_val: "Market Rates",
    card_market_sub: "Check mandi rates",
    card_disease_title: "Plant Health",
    card_disease_val: "Disease Scan",
    card_disease_sub: "Detect leaf diseases via ML",
    farm_overview: "Your Farm Overview",
    edit_profile: "Edit Profile",
    view_ml_tool: "View ML Tool",
    get_recommendation: "Get Recommendation",
    weather_advisory: "Weather Advisory",
    view_details: "View Details",
    disease_detection: "Disease Detection",
    scan: "Scan",
    upload_image: "Upload Image",
    pest_alerts: "Pest & Disease Alerts",
    view_all: "View All",
    market_prices: "Market Prices",
    view_prices: "View Reference Prices",
    notifications_title: "Agro Alerts & Notifications",
    no_unread: "All alerts reviewed",
    mark_read: "Mark all read"
  },
  hi: {
    brand_tag: "एआई कृषि सलाह एवं किसान साथी",
    know_more: "अधिक जानें • अधिक उगाएं",
    nav_dashboard: "किसान डैशबोर्ड",
    nav_profile: "किसान प्रोफ़ाइल",
    nav_crop: "फसल सलाह",
    nav_disease: "रोग जांच (स्कैन)",
    nav_weather: "मौसम पूर्वानुमान",
    nav_pest: "कीट एवं रोग जानकारी",
    nav_market: "मंडी बाजार भाव",
    nav_tips: "खेती के सुझाव",
    nav_knowledge: "कृषि ज्ञान केंद्र",
    nav_settings: "सेटिंग्स",
    logout: "लॉग आउट",
    need_advice: "सलाह चाहिए?",
    explore_resources: "हमारे संसाधन देखें",
    farmer_role: "पंजीकृत किसान",
    greeting_morning: "सुप्रभात",
    greeting_afternoon: "नमस्कार",
    greeting_evening: "शुभ संध्या",
    welcome_quote: "\"सटीक जानकारी। स्वस्थ फसलें। समृद्ध कल।\"",
    card_crop_title: "फसल सलाह",
    card_crop_val: "सर्वश्रेष्ठ फसल खोजें",
    card_crop_sub: "मिट्टी और जलवायु के आधार पर",
    card_weather_title: "मौसम पूर्वानुमान",
    card_weather_val: "मौसम सलाह देखें",
    card_weather_sub: "स्थानीय कृषि मौसम",
    card_market_title: "संदर्भ मूल्य",
    card_market_val: "मंडी बाजार भाव",
    card_market_sub: "ताज़ा मंडी भाव देखें",
    card_disease_title: "पौध स्वास्थ्य",
    card_disease_val: "रोग जांच (स्कैन)",
    card_disease_sub: "एआई द्वारा पत्ती रोग पहचान",
    farm_overview: "खेत का विवरण",
    edit_profile: "प्रोफ़ाइल बदलें",
    view_ml_tool: "एआई टूल देखें",
    get_recommendation: "फसल सलाह प्राप्त करें",
    weather_advisory: "मौसम सलाह",
    view_details: "विवरण देखें",
    disease_detection: "रोग पहचान",
    scan: "स्कैन करें",
    upload_image: "फोटो अपलोड करें",
    pest_alerts: "कीट और रोग अलर्ट",
    view_all: "सभी देखें",
    market_prices: "मंडी भाव",
    view_prices: "मंडी भाव देखें",
    notifications_title: "कृषि सूचनाएं एवं अलर्ट",
    no_unread: "सभी सूचनाएं पढ़ी जा चुकी हैं",
    mark_read: "सभी पढ़ा हुआ चिह्नित करें"
  },
  pa: {
    brand_tag: "ਏਆਈ ਖੇਤੀਬਾੜੀ ਸਲਾਹ ਅਤੇ ਕਿਸਾਨ ਸਾਥੀ",
    know_more: "ਵੱਧ ਜਾਣੋ • ਵੱਧ ਉਗਾਓ",
    nav_dashboard: "ਕਿਸਾਨ ਡੈਸ਼ਬੋਰਡ",
    nav_profile: "ਕਿਸਾਨ ਪ੍ਰੋਫਾਈਲ",
    nav_crop: "ਫ਼ਸਲ ਸਲਾਹ",
    nav_disease: "ਬੂਟਿਆਂ ਦੇ ਰੋਗ ਜਾਂਚ",
    nav_weather: "ਮੌਸਮ ਜਾਣਕਾਰੀ",
    nav_pest: "ਕੀੜੇ ਅਤੇ ਰੋਗ ਜਾਣਕਾਰੀ",
    nav_market: "ਮੰਡੀ ਦੇ ਭਾਅ",
    nav_tips: "ਖੇਤੀਬਾੜੀ ਸੁਝਾਅ",
    nav_knowledge: "ਖੇਤੀ ਗਿਆਨ ਕੇਂਦਰ",
    nav_settings: "ਸੈਟਿੰਗਾਂ",
    logout: "ਲੌਗ ਆਊਟ",
    need_advice: "ਸਲਾਹ ਚਾਹੀਦੀ ਹੈ?",
    explore_resources: "ਸਾਡੇ ਸਰੋਤ ਦੇਖੋ",
    farmer_role: "ਰਜਿਸਟਰਡ ਕਿਸਾਨ",
    greeting_morning: "ਸ਼ੁਭ ਸਵੇਰ",
    greeting_afternoon: "ਸਤ ਸ੍ਰੀ ਅਕਾਲ",
    greeting_evening: "ਸ਼ੁਭ ਸ਼ਾਮ",
    welcome_quote: "\"ਸਹੀ ਜਾਣਕਾਰੀ। ਸਿਹਤਮੰਦ ਫ਼ਸਲਾਂ। ਖੁਸ਼ਹਾਲ ਭਵਿੱਖ।\"",
    card_crop_title: "ਫ਼ਸਲ ਸਲਾਹ",
    card_crop_val: "ਵਧੀਆ ਫ਼ਸਲ ਲੱਭੋ",
    card_crop_sub: "ਮਿੱਟੀ ਅਤੇ ਮੌਸਮ ਅਨੁਸਾਰ",
    card_weather_title: "ਮੌਸਮ ਜਾਣਕਾਰੀ",
    card_weather_val: "ਮੌਸਮ ਸਲਾਹ ਦੇਖੋ",
    card_weather_sub: "ਖੇਤ ਲਈ ਸਥਾਨਕ ਮੌਸਮ",
    card_market_title: "ਮੰਡੀ ਰੇਟ",
    card_market_val: "ਤਾਜ਼ਾ ਮੰਡੀ ਭਾਅ",
    card_market_sub: "ਰੋਜ਼ਾਨਾ ਮੰਡੀ ਅਪਡੇਟ",
    card_disease_title: "ਬੂਟਿਆਂ ਦੀ ਸਿਹਤ",
    card_disease_val: "ਰੋਗ ਜਾਂਚ (ਸਕੈਨ)",
    card_disease_sub: "ਪੱਤਿਆਂ ਦੀ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ",
    farm_overview: "ਖੇਤ ਦਾ ਵੇਰਵਾ",
    edit_profile: "ਪ੍ਰੋਫਾਈਲ ਬਦਲੋ",
    view_ml_tool: "ਏਆਈ ਟੂਲ ਦੇਖੋ",
    get_recommendation: "ਫ਼ਸਲ ਸਲਾਹ ਲਓ",
    weather_advisory: "ਮੌਸਮ ਸਲਾਹ",
    view_details: "ਵੇਰਵਾ ਦੇਖੋ",
    disease_detection: "ਰੋਗ ਜਾਂਚ",
    scan: "ਸਕੈਨ ਕਰੋ",
    upload_image: "ਫੋਟੋ ਅਪਲੋਡ ਕਰੋ",
    pest_alerts: "ਕੀੜੇ ਅਤੇ ਰੋਗ ਚੇਤਾਵਨੀ",
    view_all: "ਸਾਰੇ ਦੇਖੋ",
    market_prices: "ਮੰਡੀ ਦੇ ਭਾਅ",
    view_prices: "ਮੰਡੀ ਭਾਅ ਦੇਖੋ",
    notifications_title: "ਤਾਜ਼ਾ ਖੇਤੀ ਅਲਰਟ",
    no_unread: "ਸਾਰੇ ਅਲਰਟ ਦੇਖੇ ਜਾ ਚੁੱਕੇ ਹਨ",
    mark_read: "ਸਾਰੇ ਪੜ੍ਹੇ ਮਾਰਕ ਕਰੋ"
  }
};

interface AppSettingsContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  theme: Theme;
  toggleTheme: () => void;
  setTheme: (theme: Theme) => void;
  t: (key: string) => string;
}

const AppSettingsContext = createContext<AppSettingsContextType | undefined>(undefined);

export const AppSettingsProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>(() => {
    const saved = localStorage.getItem('agrisaarthi_lang');
    return (saved === 'hi' || saved === 'pa' || saved === 'en') ? saved : 'en';
  });

  const [theme, setThemeState] = useState<Theme>(() => {
    const saved = localStorage.getItem('agrisaarthi_theme');
    return saved === 'dark' ? 'dark' : 'light';
  });

  useEffect(() => {
    localStorage.setItem('agrisaarthi_lang', language);
  }, [language]);

  useEffect(() => {
    localStorage.setItem('agrisaarthi_theme', theme);
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  const setLanguage = (lang: Language) => setLanguageState(lang);
  const setTheme = (newTheme: Theme) => setThemeState(newTheme);
  const toggleTheme = () => setThemeState(prev => (prev === 'light' ? 'dark' : 'light'));

  const t = (key: string) => {
    return translations[language]?.[key] ?? translations.en[key] ?? key;
  };

  return (
    <AppSettingsContext.Provider value={{ language, setLanguage, theme, toggleTheme, setTheme, t }}>
      {children}
    </AppSettingsContext.Provider>
  );
};

export const useAppSettings = () => {
  const ctx = useContext(AppSettingsContext);
  if (!ctx) throw new Error('useAppSettings must be used within AppSettingsProvider');
  return ctx;
};
