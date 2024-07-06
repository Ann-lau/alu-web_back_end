-- SQL script to list all bands with Glam rock as their main style, ranked by their longevity

-- Select band_name and calculate lifespan
SELECT
    band_name,
    COALESCE(split, YEAR(CURDATE())) - formed AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock' -- Ensure the main style is exactly 'Glam rock'
ORDER BY
    lifespan DESC; -- Order by longevity in descending order

