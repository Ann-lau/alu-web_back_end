-- lists all bands with Glam rock as their main style, ranked by their longevity
-- Import the table dump with columns: band_name (band name) and lifespan (years).
-- Compute lifespan using attributes formed and split.

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
