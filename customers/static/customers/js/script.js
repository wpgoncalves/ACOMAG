var vMaskPhoneBehavior = function(val) {
    return val.replace(/\D/g,'').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
optPhone = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskPhoneBehavior.apply({}, arguments), options)
    }
};

var vMaskCpfCnpjBehavior = function() {
    return django.jQuery("input[type='radio'][name='kind']:checked").val() === 'Física' ? '000.000.000-00' : '00.000.000/0000-00';
},
optCpfCnpj = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskCpfCnpjBehavior.apply({}, arguments), options)
    }
};

// console.log(django.jQuery(":th[class='field-cep']"));

django.jQuery(document).ready(function(){
    django.jQuery('.vMaskCepField').mask('00000-000');
    django.jQuery('.vMaskPhoneField').mask(vMaskPhoneBehavior, optPhone);
    django.jQuery('.vMaskCpfCnpjField').mask(vMaskCpfCnpjBehavior, optCpfCnpj);

    django.jQuery("[name='kind']").on("change", function(){
        django.jQuery("#id_cpf_cnpj").val("")
    });

    django.jQuery("#customers_form").submit(function(){
        django.jQuery("#customers_form").find(":input[class*='vMask']").unmask();
    });
    django.jQuery("#adresses_form").submit(function(){
        django.jQuery("#adresses_form").find(":input[class*='vMask']").unmask();
    });
    django.jQuery("#phones_form").submit(function(){
        django.jQuery("#phones_form").find(":input[class*='vMask']").unmask();
    });
});