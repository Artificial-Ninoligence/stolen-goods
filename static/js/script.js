// some scripts

// jquery ready start
$(document).ready(function() {
	// jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE,
    For sliders, interactions and other

    */ ///////////////////////////////////////


	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if





});
// jquery end

setTimeout(function(){
  $('#message').fadeOut('slow')
}, 4000)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

let amount = "{{ grand_total }}"
let url = "{% url 'payments' %}"
let csrftoken = getCookie('csrftoken');
let orderID = "{{order.order_number}}"
let payment_method = 'PayPal'
let redirect_url = "{% url 'order_complete' %}"

// Render the PayPal button into #paypal-button-container
paypal.Buttons({

	style: {
		color: 'blue',
		shape: 'rect',
		label: 'pay',
		height: 40
	},

	// Set up the transaction
	createOrder: function(data, actions) {
		return actions.order.create({
			purchase_units: [{
				amount: {
					value: amount,
				}
			}]
		});
	},

	// Finalize the transaction
	onApprove: function(data, actions) {

		return actions.order.capture().then(function(details) {
			// Show a success message to the buyer
			console.log(details);
			sendData();
			function sendData(){
				fetch(url, {
					method : "POST",
					headers: {
						"Content-type": "application/json",
						"X-CSRFToken": csrftoken,
					},
					body: JSON.stringify({
						orderID: orderID,
						transID: details.id,
						payment_method: payment_method,
						status: details.status,
					}),
				})
				.then((response) => response.json())
				.then((data) => {
				    window.location.href = redirect_url + '?order_number='+data.order_number+'&payment_id='+data.transID;
				});
			}
		});
	}
}).render('#paypal-button-container');