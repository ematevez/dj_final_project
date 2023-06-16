
var SouthVisionApp = window.SouthVisionApp || {};

(function(namespace, window, document, $, undefined) {
    "use strict";

  var defaults = {
            url: undefined,
            columns: undefined,
            dom: '<"toolbar">frtip',
            sorting: [[ 0, "desc" ]],
            table_el: '#dataTable',
            filter_el: ".table-filters",
            search_el: '#search_text',
            delete_modal_el: '#ConfirmDeleteModal',
            extraParams: undefined,
            afterLoad: undefined
        };

  var SVTable = function() {
    var self = this

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", self.getCSRF());
        }
    });
  }

  SVTable.prototype.getCSRF = function() {
    var name = 'csrftoken',  cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  SVTable.prototype.delete = function(delete_url) {
     $.ajax({
       type: "DELETE",
       url: delete_url,
       data: {},
       dataType: 'json'
     });
  };

  SVTable.prototype.init = function(options) {
    var self = this;
    this.options = $.extend({}, defaults, options);

    window.igDataTable = $('#igDataTable').DataTable({
        "responsive": true,
        "bSort": false,
        "bProcessing": true,
    	  "bServerSide": true,
        "iDisplayLength": 50,
        "aoColumns": this.options.columns,
        "aaSorting": this.options.sorting,
        "sAjaxSource": this.options.url,
        "fnServerParams": this.options.extraParams,
        "language": {
          "sProcessing":     "Procesando...",
          "sLengthMenu":     "Mostrar _MENU_ registros",
          "sZeroRecords":    "No se encontraron resultados",
          "sEmptyTable":     "Ningún dato disponible en esta entidad",
          "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
          "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
          "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
          "sInfoPostFix":    "",
          "sSearch":         "Buscar:",
          "sUrl":            "",
          "sInfoThousands":  ",",
          "sLoadingRecords": "Cargando...",
          "oPaginate": {
              "sFirst":    "Primero",
              "sLast":     "Último",
              "sNext":     "<i class=\"fa fa-chevron-right\"></i>",
              "sPrevious": "<i class=\"fa fa-chevron-left\"></i>"
          },
          "oAria": {
              "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
              "sSortDescending": ": Activar para ordenar la columna de manera descendente"
          },
        },
        "dom": this.options.dom,
		    "fnDrawCallback": function (oSettings) {
          if (self.options.afterLoad && typeof self.options.afterLoad === 'function' ) {
                self.options.afterLoad()
          }
		    }
    });
  }

  $(window).on('load', function() {
    var selected_item;
    setTimeout(function() {
        $('#ig-toolbar').show().appendTo($("div.toolbar"));
    }, 300);

    $('#igDataTable tbody').on( 'click', '.btn-delete', function (ev) {
      ev.preventDefault();
      selected_item = $(this);
    })

    $('#delete-modal .btn-danger').click( function () {
     $.ajax({
       type: "DELETE",
       url: selected_item.data('url'),
       data: {},
       success: function(response) {
         if (response.status_ok) {
          window.igDataTable.row(selected_item.closest('tr')).remove().draw( false );
         }
         else {
          $.niftyNoty({
              type: 'danger',
              container: 'page',
              html: response.message,
              floating: {
                  position: "top-left",
                  animationIn: "bounceInDown",
                  animationOut: "fadeOut"
              },
              focus: true,
              timer: 2500
          });
         }
          $('#delete-modal').modal('hide');
       },
       dataType: 'json'
     });

    });

  });

  namespace.DataTable = new SVTable();


})(SouthVisionApp, window, window.document, window.jQuery);
