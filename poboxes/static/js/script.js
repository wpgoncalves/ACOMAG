django.jQuery(document).ready(function(){
    django.jQuery(".vMaskCpfField").mask("000.000.000-00", {reverse:true});
    django.jQuery(".vMaskDateField").mask("00/00/0000");

    django.jQuery("#customer_form").submit(function(){
        django.jQuery("#customer_form").find(":input[id='id_cpf']").unmask();
    });
});