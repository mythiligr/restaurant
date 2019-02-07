$("#repeater1").createRepeater({
    showFirstItemToDefault: true,
});


$("#submit-options").click(function(event) {
    var table = [];
    highlightDuplicates('form-table');
    if (error1 == false) {
        table = $(".options").map(function() {
            return $(this).val();
        }).get();
        tables_id = $(".options").map(function() {
            return $(this).attr("data-id");
        }).get();
        // Validation
        var error = false;
        $("#form-table").find("textarea").each(function() {
            if (!this.value) {
                $(this).css({
                    "border-color": "red"
                });
                error = true;
            } else {
                $(this).css({
                    "border-color": ""
                });
            }
        });
        if (error == false) {
            submit_tables(table, tables_id);
        }
    } else {
        alert('Value should be unique!!');
    }
    event.preventDefault();
    return false;
});

function highlightDuplicates(id, type="") {
    error1 = false;
    $('#' + id).find('textarea').each(function() {
        errorCount = 0;
        var thisVal = $(this);
        var value = $(this).val();
        validate(value, id);
        if (errorCount > 1) {
            thisVal.css({
                "border-color": "red"
            });
            error1 = true;
        } else {
            thisVal.css({
                "border-color": ""
            });
        }
    });
}

function validate(value, id) {
    $('#' + id).find('textarea').each(function() {
        if ($(this).val() != '' && ($.trim(value.toLowerCase()) == $.trim($(this).val().toLowerCase()))) {
            errorCount = errorCount + 1
        }
    })
}

function submit_tables(dta, dta_id) {
    $.ajax({
        type: "POST",
        url: "/Create-table/",
        data: {
            'form_data': dta,
            'form_data_id': dta_id,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function(response) {
            if (response.status != false) {
                window.location.href = "/Book-table/";
            }
        }
    });
    event.preventDefault();
}