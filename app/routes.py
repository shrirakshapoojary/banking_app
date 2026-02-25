from flask import Blueprint, render_template, request, redirect
from .database import SessionLocal
from .models import Account, Transaction

main = Blueprint("main", __name__)

# Home – show accounts
@main.route("/")
def index():
    session = SessionLocal()
    accounts = session.query(Account).all()
    session.close()
    return render_template("index.html", accounts=accounts)

# Create account
@main.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        session = SessionLocal()
        acc = Account(name=name, balance=0)
        session.add(acc)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("create_account.html")

# Deposit
@main.route("/deposit/<int:id>", methods=["GET", "POST"])
def deposit(id):
    session = SessionLocal()
    acc = session.query(Account).get(id)

    if request.method == "POST":
        amount = int(request.form["amount"])
        acc.balance += amount
        session.add(Transaction(account_id=id, amount=amount, type="deposit"))
        session.commit()
        session.close()
        return redirect("/")

    return render_template("deposit.html", account=acc)

# Withdraw
@main.route("/withdraw/<int:id>", methods=["GET", "POST"])
def withdraw(id):
    session = SessionLocal()
    acc = session.query(Account).get(id)

    if request.method == "POST":
        amount = int(request.form["amount"])
        if acc.balance >= amount:
            acc.balance -= amount
            session.add(Transaction(account_id=id, amount=amount, type="withdraw"))
            session.commit()
        session.close()
        return redirect("/")

    return render_template("withdraw.html", account=acc)