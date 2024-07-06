-- SQL script to list all bands with Glam rock as their main style, ranked by their longevity

-- Ensure the table metal_bands is imported
-- Assuming the table metal_bands has columns: band_name, formed, split, and style

-- Select band_name and calculate lifespan
SELECT
    band_name,
    COALESCE(split, YEAR(CURDATE())) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE 'Glam rock%' -- Check if Glam rock is the main style
ORDER BY
    lifespan DESC; -- Order by longevity in descending order

