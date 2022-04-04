var vMaskPhoneBehavior = function(val) {
    return val.replace(/\D/g,"").length === 11 ? "(00) 00000-0000" : "(00) 0000-00009";
},
optPhone = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskPhoneBehavior.apply({}, arguments), options)
    }
};

var vMaskCpfCnpjBehavior = function() {
    return django.jQuery("input[type='radio'][name='kind']:checked").val() === "Física" ? "000.000.000-00" : "00.000.000/0000-00";
},
optCpfCnpj = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskCpfCnpjBehavior.apply({}, arguments), options)
    }
};

var vMaskPhoneTh = function(val) {
    return val.replace(/\D/g,"").length === 11 ? "(00) 00000-0000" : "(00) 0000-00009";
};

var vMaskCpfCnpjBehaviorTh = function(val) {
    return val.replace(/\D/g,"").length === 11 ? "000.000.000-00" : "00.000.000/0000-00";
};

django.jQuery(document).ready(function() {
    // Aplica máscaras aos campos de formulário (Cep, Telefone e CPF/CNPJ).
    django.jQuery(".vMaskCepField").mask("00000-000");
    django.jQuery(".vMaskPhoneField").mask(vMaskPhoneBehavior, optPhone);
    django.jQuery(".vMaskCpfCnpjField").mask(vMaskCpfCnpjBehavior, optCpfCnpj);
    
    // Aplica máscaras aos campos da lista para visualização (Cep, Telefone e CPF/CNPJ).
    django.jQuery("td[class='field-cep']").attr("class", "field-cep vMaskCepTh");
    django.jQuery(".vMaskCepTh").mask("00000-000");
    // django.jQuery("body[class*='model-phones']").find("div[id='content']").find("h2").attr("class", "vMaskPhoneTh");
    django.jQuery("td[class='field-number']").attr("class", "field-number vMaskPhoneTh");
    django.jQuery(".vMaskPhoneTh").mask(vMaskPhoneTh);
    django.jQuery("td[class='field-cpf_cnpj']").attr("class", "field-cpf_cnpj vMaskCpfCnpjTh");
    django.jQuery(".vMaskCpfCnpjTh").mask(vMaskCpfCnpjBehaviorTh);

    //Atualiza o campo especifico após realizada alteração nas opções de tipo.
    django.jQuery("[name='kind']").on("change", function() {
        django.jQuery("#id_cpf_cnpj").val("")
    });

    // Ao submeter o formulário para salvamento das informações é retirada a máscara dos valores dos campos.
    django.jQuery("#customers_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
    django.jQuery("#adresses_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
    django.jQuery("#phones_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
});