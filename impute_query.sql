# This query assumes that there is a pre-declared function "median".
# It also imputes non-matched null values with 0.

update country_vaccination_stats
inner join (
    select country, median(daily_vaccinations) as median_daily_vaccinations
    from country_vaccination_stats
    group by country
) b on country_vaccination_stats.country = b.country
set daily_vaccinations = b.median_daily_vaccinations
where daily_vaccinations = "";
