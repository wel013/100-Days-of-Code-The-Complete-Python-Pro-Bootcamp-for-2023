from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# CREATE DB


class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def convert_to_dict(self):
        dictionary = {}
        for col in self.__table__.columns:
            dictionary[col.name] = getattr(self, col.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=["GET"])
def get_random_cafe():
    total = db.session.query(func.count(Cafe.id)).scalar()
    print(f"total is {total} cafes")
    rand_num = random.randint(0, total)
    res = db.session.execute(db.select(Cafe)).scalars().all()[rand_num]
    # res_json = {"cafe_id": res.id, "name": res.name, "map_url": res.map_url, "img_url": res.img_url,
    #             "location": res.location, "seats": res.seats, "has_toilet": res.has_toilet, "has_wifi": res.has_wifi,
    #             "has_sockets": res.has_sockets, "can_take_calls": res.can_take_calls, "coffee_price": res.coffee_price, }
    res_dict = res.convert_to_dict()
    return jsonify(res_dict)


@app.route('/all', methods=["GET"])
def get_all_cafes():
    res = db.session.execute(db.select(Cafe)).scalars().all()
    res_list = [cafe.convert_to_dict() for cafe in res]
    # res_json = {"cafe_id": res.id, "name": res.name, "map_url": res.map_url, "img_url": res.img_url,
    #             "location": res.location, "seats": res.seats, "has_toilet": res.has_toilet, "has_wifi": res.has_wifi,
    #             "has_sockets": res.has_sockets, "can_take_calls": res.can_take_calls, "coffee_price": res.coffee_price, }
    final_dict = {"cafes": res_list}
    return jsonify(final_dict)


@app.route('/search', methods=["GET"])
def search_cafe():
    loc = request.args.get("loc")
    res = db.session.execute(db.select(Cafe).where(
        Cafe.location == loc)).scalars().all()
    not_found = {"Not Found": "Sorry, we don't have a cafe at the location."}
    if not res:
        return jsonify({"error": not_found}), 404
    else:
        res_list = [cafe.convert_to_dict() for cafe in res]
        final_dict = {"cafes": res_list}
        return jsonify(final_dict)

# HTTP POST - Create Record


@app.route('/add', methods=["POST"])
def add_cafe():
    # get all request parameters and creates a new SQLAlchemy obj
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    if new_cafe:
        db.session.add(new_cafe)
        db.session.commit()
        success = {"success": "Successfully added the new cafe."}
        return jsonify({"response": success})
    else:
        failure = {
            "failure": "Could not add your cafe."}
        return jsonify({"response": failure})

# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    try:
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        success = {"success": "Successfully updated the price."}
        return jsonify({"response": success})
    except NotFound:
        failure = {
            "Not Found": "Sorry a cafe with that id was not found in the database."}
        return jsonify({"error": failure}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != "TopSecretAPIKey":
        return jsonify({"error": "Sorry, your are not authorized. Please make sure you have the correct api_key."})
    else:
        try:
            cafe_to_del = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe_to_del)
            db.session.commit()
            success = {"success": "Successfully deleted the closed cafe."}
            return jsonify({"response": success})
        except NotFound:
            failure = {
                "Not Found": "Sorry a cafe with that id was not found in the database."}
            return jsonify({"error": failure}), 404


if __name__ == '__main__':
    app.run(debug=True)


#Documentation: 
# https://documenter.getpostman.com/view/33538725/2sA3dxErwS