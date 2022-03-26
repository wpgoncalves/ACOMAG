var options =  {
    onKeyPress: function(val, e, field, options) {
        var masks = ['000.000.000-009', '00.000.000/0000-00'];
        var mask = (val.length>14) ? masks[1] : masks[0];
        django.jQuery('.vMaskCpfCnpjField').mask(mask, options);
  
}};

django.jQuery(document).ready(function(){
    django.jQuery(".vMaskDateField").mask("00/00/0000");
    django.jQuery('.vMaskCpfCnpjField').mask('000.000.000-009', options);

    django.jQuery("#customer_form").submit(function(){
        django.jQuery("#customer_form").find(":input[class*='vMaskC']").unmask();
    });
});