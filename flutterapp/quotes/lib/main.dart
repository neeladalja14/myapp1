import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: QuoteList(),
));


class QuoteList extends StatefulWidget {
  @override
  _QuoteListState createState() => _QuoteListState();
}

class _QuoteListState extends State<QuoteList> {

  List<String> qoutes =[
    "Be Yourself; Everyone Else Is Already Taken",
    "I Have Nothing to Declare Except My Genius",
    "The Truth Is Rarely Pure And Never Simple"
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      appBar: AppBar(
        title: Text("Awesome Quotes"),
        centerTitle: true,
        backgroundColor: Colors.redAccent,
      ),
      body: Column(
        children: qoutes.map((quote) => Text(quote)).toList(),
      )
    );
  }
}
