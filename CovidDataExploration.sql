Select *
From CovidDeaths
Where location like '%India%'
order by 3,4

-- Select Data that we are going to be starting with

Select Location, date, total_cases, new_cases, total_deaths
From PortfolioProject..CovidDeaths
Where continent is not null
order by 1,2

-- Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country

Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercent
From CovidDeaths
Where Location Like '%India%'
and Continent is Not NULL
Order By 1,2

-- Looking at Total Cases vs Population
-- Shows what percentage of population got covid

Select location, date, total_cases, population, (total_cases/population)*100 as PercentPopulationInfected
From CovidDeaths
Where Location Like '%India%'
and Continent is Not NULL
Order By 1,2

-- Countries with Highest Infection Rate compared to Population

Select location, Population, Max(total_cases) as HighestInfectionCount,(Max(total_cases/population))*100 as PercentPopulationInfected
From CovidDeaths
Where Continent is Not NULL
Group By Location, Population
Order By PercentPopulationInfected Desc

-- Countries with Highest Death Count per Population

Select location, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where Continent is Not NULL
Group By Location
Order By TotalDeathCount Desc

-- BREAKING THINGS DOWN BY CONTINENT

-- Showing contintents with the highest death count per population

Select Continent, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where Continent is Not NULL
Group By Continent
Order By TotalDeathCount Desc


--GLOBAL NUMBERS

Select SUM(new_cases) as total_cases, SUM(new_deaths) as total_deaths, SUM(new_deaths)/SUM(New_Cases)*100 as DeathPercentage
From PortfolioProject..CovidDeaths
--Where location like '%states%'
where continent is not null 
--Group By date
order by 1,2

-- Total Population vs Vaccinations
-- Shows Percentage of Population that has recieved at least one Covid Vaccine

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, Sum(Convert(Int,vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date) as RollingPeopleVaccinated
From CovidDeaths dea 
Join CovidVaccinations vac 
ON dea.location = vac.location
and dea.date = vac.date
Where dea.continent is not null
Order By 2,3

-- Using CTE to perform Calculation on Partition By in previous query

With PopvsVac (Continent, loaction, date,population, new_vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, Sum(Convert(Int,vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date) as RollingPeopleVaccinated
From CovidDeaths dea 
Join CovidVaccinations vac 
ON dea.location = vac.location
and dea.date = vac.date
Where dea.continent is not null
--Order By 2,3
)
Select*, (RollingPeopleVaccinated/population)*100 as PercentPopulationVaccinated
From PopvsVac
Order By 2,3

-- Using Temp Table to perform Calculation on Partition By in previous query


Drop Table if exists #PercenetPopulationVaccinated
Create Table #PercenetPopulationVaccinated
(Continent varchar (50),
 Location  varchar (50),
 Date      datetime,
 Population numeric,
 New_vaccination numeric,
 RollingPeoplevaccinated numeric
)

Insert Into #PercenetPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, Sum(Convert(Int,vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date) as RollingPeopleVaccinated
From CovidDeaths dea 
Join CovidVaccinations vac 
ON dea.location = vac.location
and dea.date = vac.date
--Where dea.continent is not null
--Order By 2,3


Select *, (RollingPeopleVaccinated/Population)*100
From #PercenetPopulationVaccinated

-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, Sum(Convert(Int,vac.new_vaccinations)) OVER (Partition By dea.location Order By dea.location, dea.date) as RollingPeopleVaccinated
From CovidDeaths dea 
Join CovidVaccinations vac 
ON dea.location = vac.location
and dea.date = vac.date
Where dea.continent is not null