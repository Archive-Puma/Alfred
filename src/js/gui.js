function GUI()
{
    this.height = 50;
    this.buttons = [];

    var play = new Button("Empezar", 60, this.height/2);
    play.onClick = function() {}
    this.buttons.push(play);

    this.show = function()
    {
        noStroke();
        fill(color(21,27,34));
        rect(width/2,this.height/2,width,this.height);
        
        for(var button of this.buttons)
        {
            button.show();
        }
    }
}


function Button(txt, offsetX, y)
{
    this.text = txt;
    this.offsetX = offsetX;
    this.position = createVector(width - offsetX, 25);
    this.size = createVector(100,30);
    this.boxColor = { off: color(205,210,205) };
    this.textColor = color(41,47,54);

    this.resize = function()
    {
        this.position.x = width - this.offsetX;
    }

    this.show = function()
    {
        noStroke();
        fill(this.boxColor.off);
        rect(this.position.x, this.position.y, this.size.x, this.size.y, 20);

        fill(this.textColor);
        text(this.text, this.position.x, this.position.y + 4);
    }
}