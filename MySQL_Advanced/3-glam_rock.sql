-- SQL script to list all bands with Glam rock as their main style, ranked by their longevity

-- Select band_name and calculate lifespan
SELECT
    band_name,
    COALESCE(split, 2022) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%' -- Check if Glam rock is the main style
ORDER BY
    lifespan DESC; -- Order by longevity in descending order
