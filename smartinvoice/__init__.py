from .utils import send_api_request
from initialization.models import Configurations

class Smart_Invoice_Integration:
    def __init__ (self):
        config = Configurations.objects.all ().first ()
        self.baseurl = config.vsdc_url if config else ""

    def generate_url (self, url):
        return f"{self.baseurl}/{url}"

    def stock_item (self, data: dict):
        stock_item: dict = data.get ("stock_item")
        stock_master: dict = data.get ("stock_master")
        res = send_api_request ("POST", self.generate_url (stock_item.get ("url"), json=stock_item.get("data")))
        if not res or res.get ("resultCd") != "000" and res.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Item"}
        sm_res = send_api_request ("POST", self.generate_url (stock_master.get ("url"), json=stock_master.get("data")))
        if not sm_res or sm_res.get ("resultCd") != "000" and sm_res.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Master"}
        return {"status": True, "msg": "Succeeded"}

    def si_item (self, data: dict):
        res = send_api_request ("POST", self.generate_url (data.get ("url"), json=data.get("data")))
        if not res or res.get ("resultCd") != "000" and res.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Item Saving"}
        return {"status": True, "msg": "Succeeded"}

    def si_general_request (self, type:str, data: dict):
        res = send_api_request ("POST", self.generate_url (data.get ("url"), json=data.get("data")))
        if not res or res.get ("resultCd") != "000" and res.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": type}
        return {"status": True, "msg": "Succeeded"}

    def sales (self, data: dict):
        sale: dict = data.get ("sale")
        stock_item: dict = data.get ("stock_item")
        stock_master: dict = data.get ("stock_master")
        sale_transaction = send_api_request ("POST", self.generate_url (sale.get ("url"), json=sale.get("data")))
        if not sale_transaction or sale_transaction.get ("resultCd") != "000" and sale_transaction.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Sale Transaction"}
        st_itm = send_api_request ("POST", self.generate_url (stock_item.get ("url"), json=stock_item.get("data")))
        if not st_itm or st_itm.get ("resultCd") != "000" and st_itm.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Item"}
        st_mast = send_api_request ("POST", self.generate_url (stock_master.get ("url"), json=stock_master.get("data")))
        if not st_mast or st_mast.get ("resultCd") != "000" and st_mast.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Item"}
        return {"status": True, "msg": "Succeeded"}

    def purchase (self, data: dict):
        purchase: dict = data.get ("purchase")
        stock_item: dict = data.get ("stock_item")
        stock_master: dict = data.get ("stock_master")
        purchase_transaction = send_api_request ("POST", self.generate_url (purchase.get ("url"), json=purchase.get("data")))
        if not purchase_transaction or purchase_transaction.get ("resultCd") != "000" and purchase_transaction.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Purchase Transaction"}
        st_itm = send_api_request ("POST", self.generate_url (stock_item.get ("url"), json=stock_item.get("data")))
        if not st_itm or st_itm.get ("resultCd") != "000" and st_itm.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Item"}
        st_mast = send_api_request ("POST", self.generate_url (stock_master.get ("url"), json=stock_master.get("data")))
        if not st_mast or st_mast.get ("resultCd") != "000" and st_mast.get ("resultMsg") != "It is succeeded":
            return {"status": False, "msg": "Stock Item"}
        return {"status": True, "msg": "Succeeded"}