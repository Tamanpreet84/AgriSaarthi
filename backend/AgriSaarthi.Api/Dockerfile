# ==============================================================================
# Multi-stage Dockerfile for AgriSaarthi.Api (ASP.NET Core 10)
# ==============================================================================
FROM mcr.microsoft.com/dotnet/sdk:10.0-preview AS build
WORKDIR /src

# Copy project files and restore dependencies
COPY ["backend/AgriSaarthi.Api/AgriSaarthi.Api.csproj", "backend/AgriSaarthi.Api/"]
RUN dotnet restore "backend/AgriSaarthi.Api/AgriSaarthi.Api.csproj"

# Copy full source and publish Release build
COPY backend/AgriSaarthi.Api/ backend/AgriSaarthi.Api/
WORKDIR "/src/backend/AgriSaarthi.Api"
RUN dotnet publish "AgriSaarthi.Api.csproj" -c Release -o /app/publish /p:UseAppHost=false

# ==============================================================================
# Production Runtime Image
# ==============================================================================
FROM mcr.microsoft.com/dotnet/aspnet:10.0-preview AS final
WORKDIR /app
COPY --from=build /app/publish .

# Set default ASP.NET Core environment
ENV ASPNETCORE_ENVIRONMENT=Production

# Port 5000 is default; overridden dynamically by PORT env var on Render / Railway
EXPOSE 5000

ENTRYPOINT ["dotnet", "AgriSaarthi.Api.dll"]
