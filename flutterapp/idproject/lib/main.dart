import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: Idproject(),
));

class Idproject extends StatefulWidget {
  @override
  _IdprojectState createState() => _IdprojectState();
}

class _IdprojectState extends State<Idproject> {

  int ninjalevel = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[900],
      appBar: AppBar(
        title: Text("Idapp project"),
        centerTitle: true,
        backgroundColor: Colors.grey[850],
        elevation: 0.0,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            ninjalevel += 1;
          });
        },
        child: Icon(Icons.add),
        backgroundColor: Colors.grey[800],
      ),
      body: Padding(
        padding: EdgeInsets.fromLTRB(30.0, 40.0, 30.0, 0.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Center(
              child: CircleAvatar(
                backgroundImage: AssetImage('assets/thumb.png'),
                radius: 40.0,
              ),
            ),
            Divider(
              height: 90.0,
              color: Colors.grey[800],
            ),
            Text(
            'NAME',
            style: TextStyle(
              color: Colors.grey,
              letterSpacing: 2.0,
            )
            ),
            SizedBox(height: 10.0,),
            Text(
              'Neel-Aa',
              style: TextStyle(
                color: Colors.amberAccent[200],
                letterSpacing: 2.0,
                fontSize: 28.0,
                fontWeight: FontWeight.bold
              )
            ),
            SizedBox(height: 30.0,),
            Text(
              'CURRENT NINJA LEVEL',
                style: TextStyle(
                  color: Colors.grey,
                  letterSpacing: 2.0,
                  )
            ),
            SizedBox(height: 10.0,),
            Text(
              '$ninjalevel',
                style: TextStyle(
                  color: Colors.amberAccent[200],
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold
                )
            ),
            SizedBox(height: 30.0),
            Row(
              children: <Widget>[
                Icon(
                  Icons.email,
                  color: Colors.red,
                ),
                SizedBox(width: 10.0),
                Text(
                  'neeladalja@gmail.com',
                  style: TextStyle(
                    color: Colors.grey[400],
                    fontSize: 18.0,
                    letterSpacing: 1.0,
                  ),
                ),
              ],
            ),
          ],
        )
      )
    );
  }
}


class Test extends StatefulWidget {
  @override
  _TestState createState() => _TestState();
}

class _TestState extends State<Test> {

  int counter = 1;

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
