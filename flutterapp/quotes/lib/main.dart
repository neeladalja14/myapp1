import 'package:flutter/material.dart';
import 'quote.dart';

void main() => runApp(MaterialApp(
  home: QuoteList(),
));


class QuoteList extends StatefulWidget {
  @override
  _QuoteListState createState() => _QuoteListState();
}

class _QuoteListState extends State<QuoteList> {

  List<Quote> qoutes =[
    Quote(author: 'oscar wilde', text: 'Be yourself, eveyone else is already taken'),
    Quote(author: 'oscar wilde', text: 'i have a nothing to declare except my genius'),
    Quote(author: 'oscar wilde', text: 'The truth is Rarely pure amd never simple'),
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
        children: qoutes.map((quote) => Text('${quote.text} - ${quote.author}')).toList(),
      )
    );
  }
}
