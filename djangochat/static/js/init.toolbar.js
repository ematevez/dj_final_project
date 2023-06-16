var timeout;

function initToolbar() {
    if (USER_SECTION!==UNIDHO) {
        $('#tool_section').attr('disabled','disabled');;
        if (USER_SECTOR!==ALL_SECTORS) {
            $('#tool_sector').attr('disabled','disabled');;
        }
    }
}

$(document).ready(function() {

    $('#tool_section').val(USER_SECTION);
    $('#tool_sector').val(USER_SECTOR);

    $('input[type=search]').on( 'keyup', function () {
        var val = this.value;
        clearTimeout(timeout);
        timeout = setTimeout(function() {
            igDataTable.search(val).draw();
            clearTimeout(timeout);
        }, 300);
    });

    $("select").select2({
        minimumResultsForSearch: -1,
        width: '200px'
    }).on('change', function () {
      igDataTable.ajax.reload();
    });

  $('#tool_date').daterangepicker({
    autoUpdateInput: false,
    locale: {
      cancelLabel: 'Limpiar',
      applyLabel: 'Aplicar'
    }
  });

  $('#tool_date').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
      igDataTable.ajax.reload();
  });

  $('#tool_date').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
      igDataTable.ajax.reload();
  });


    setTimeout(initToolbar, 100);
});
