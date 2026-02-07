from flask import request, jsonify
from flask_login import login_required, current_user
from app.core.services.premium_service import PremiumService
from app.core.services.coins_service import CoinsService

def register(api):
    @api.route("/premium/buy", methods=["POST"])
    @login_required
    def buy():
        days = request.json.get("days")
        price = request.json.get("price")

        if current_user.coins_balance < price:
            return jsonify({"error": "Not enough coins"}), 400

        CoinsService.remove_coins(current_user, price, "Premium purchase")
        PremiumService.activate(current_user, days, price)

        return jsonify({"status": "ok"})
