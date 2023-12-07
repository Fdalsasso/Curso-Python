insert into cliente VALUES (1, "gustavo", "Dalsasso", "Mercado Pago", 2001);

delete from cliente;

update cliente
set fecha_de_nacimiento = 2001
where idcliente = 1;

select * from cliente;