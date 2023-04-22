$(document).ready(function (){

    $('.table').paging({limit:5});

    $('#table-demo').paging({

        limit: 5,
        rowDisplayStyle: 'block',
        activePage: 0,
        rows: []

        });
    NProgress.start();
    NProgress.done();

     $(".datetimeinput").datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});

});
