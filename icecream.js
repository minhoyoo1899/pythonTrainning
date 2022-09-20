let members = 29;
let price = 1000;
let result = members * price;

//console.log(result);
function icecreamPrice(l_members, l_price) {
  let vat = 10 % l_price + l_price;
  return l_members * vat;
}

function icecreamPriceB(l_members, l_price) {
  return l_members * l_price + 1000;
}

//console.log(icecreamPrice(100, 100));

console.log(icecreamPriceB(30, 1000));