from config.next_gen_lead_config import *
from models.product_equiry_model import  *
from models.dealer_model import *

@app.route('/fetch-todays-leads', methods=['GET'])
def fetchTodaysLeads():
    """Returns the leads info for current date.."""
    log.info("fetchTodaysLeads : Started")
    currentdate = date.today()
    log.debug("Currentdate is {}".format(currentdate))
    dealer_code = request.args.get('dealer_code')
    log.debug("dealer_code is {}".format(dealer_code))

    try:
        dealer_result = session.query(Dealer).filter(Dealer.dealerCode == dealer_code).all()
        log.debug("dealer_result is {}".format(dealer_result))

    except Exception as err:
        log.error("Error occured while dealer table sql transaction is {}".format(err))
        session.rollback()

    if dealer_result:
        try:
            product_result = session.query(ProductEnquiry). \
                filter(ProductEnquiry.createdDate == str(currentdate),
                       ProductEnquiry.dealerCode == request.args.get('dealer_code')).all()
            log.debug("product_result is {}".format(product_result))
        except Exception as err:
            session.rollback()
            log.error("Error occured while ProductEnquiry table sql transaction is {}".format(err))
        finally:
            session.close()
        product_result_dict = [item.__dict__ for item in product_result]
        log.debug("product_result_dict is {}".format(product_result_dict))
        for item in product_result_dict:
            del item['_sa_instance_state']
        log.info("fetchTodaysLeads : Ended")
        return jsonify(product_result_dict)
    else:
        log.info("fetchTodaysLeads : Ended")
        return "Unauthorized access"

# Run the APP
app.run(debug=False)

