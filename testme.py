from flask import Flask, request
app= Flask(__name__)
app.config['DEBUG']= True
@app.route("/")
def movielist():
    listmovie=["Jesus", "God", "Holy Spirit", "The vatican","Boundage", "Hacker", "Final","The Time", "Blessing", "The new age","The Engels", "Delivrance", "Victory"]        
    dropdown_movie= """
        <form action="/dropdown" method="post">
            <label for="new-movie">
                <select>
                    <option value="Rambo">Rambo</option>
                    <option value="Son of God">{h}</option>
##                    <option value="Passion of Christ">Passion of Christ</option>
##                    <option value="John Paul II">Carol Vojtila</option>
##                    <option value="HolySpirit">The Holy Spirit</option>
##                    <option value="moovie" selected> </option>
                </select>
                from my Watchlist.
            </label>
            <input type="submit" value="choose your moovie"/>
        </form>

        """
    h=""
    for i in range(len(listmovie)):
        h=listmovie[i]
        return dropdown_movie
app.run()
