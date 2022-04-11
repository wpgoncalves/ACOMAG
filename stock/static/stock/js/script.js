django.jQuery(document).ready(function() {
    // Aplica máscaras ao campo code do formulário.
    django.jQuery(".vMaskCodeField").mask("000000000");
    django.jQuery(".vMaskRegistrationField").mask("0.000.000-0");

    // Aplica máscaras aos campos da lista para visualização (Cep, Telefone e CPF/CNPJ).
    django.jQuery("td[class='field-registration']").attr("class", "field-registration vMaskRegistrationTh");
    django.jQuery(".vMaskRegistrationTh").mask("0.000.000-0");
    
    // Ao submeter o formulário para salvamento das informações é retirada a máscara dos valores dos campos.
    django.jQuery("#items_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
    django.jQuery("#holders_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
});