function update_result_price(){
	var count, price;
	var result = "";

	count = $("#id_count_product").val();
	price = $("#price-product").text();
	result = count * price;

	$("#count-product").text(count);
	$("#result-price-product").text(result + " руб.");
}

$(document).ready(function() {
	update_result_price();
});


$("#id_count_product").change( function() {
  update_result_price();
});