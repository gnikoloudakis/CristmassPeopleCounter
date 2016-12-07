/**
 * Created by yannisnikoloudakis on 04/12/16.
 */
$(function () {
    $('#pause_counter').on('click', function () {
        $('#resume_counter').prop('disabled', false);
        $(this).prop('disabled', true);
        $('#control_text').html('Counting Paused');
    });

    $('#resume_counter').on('click', function () {
        $('#pause_counter').prop('disabled', false);
        $(this).prop('disabled', true);
        $('#control_text').html('Counting Resumed');
    });


    $('#set_counter_1').on('click', function () {
        $('#set_counter_2').prop('disabled', false);
        $(this).prop('disabled', true);
    });

    $('#set_counter_2').on('click', function () {
        $('#set_counter_3').prop('disabled', false);
        $(this).prop('disabled', true);
    });

    $('#set_counter_3').on('click', function () {
        var counter_value = $('#set_counter').val();
        if (counter_value != '') {
            $('#set_counter_1').prop('disabled', false);
            $(this).prop('disabled', true);

            $.ajax({
                url: '/set_counter',
                type: 'POST',
                data: {
                    counter: counter_value
                },
                cache: false,
                success: function () {
                    $('#set_text').html('Counter set to ' + counter_value);
                },
                error: function () {
                    $('#set_text').html('Unable to set value...');
                }
            });
        }
        else {
            $('#set_text').html('Please .... Enter a value to Set!!!');

        }
    });

    $('#reset_1').on('click', function () {
        $('#reset_2').prop('disabled', false);
        $(this).prop('disabled', true);
    });

    $('#reset_2').on('click', function () {
        $('#reset_3').prop('disabled', false);
        $(this).prop('disabled', true);
    });
    $('#reset_3').on('click', function () {
        $('#reset_1').prop('disabled', false);
        $(this).prop('disabled', true);
        $('#reset_text').html('Counter has been reset');
    });



});