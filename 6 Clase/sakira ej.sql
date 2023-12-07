SELECT store.store_id as sucursal, address.address as direccion, country.country as pais, city.city as city FROM store
JOIN address ON address.address_id = store.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id;