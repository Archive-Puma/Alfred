function Link(from, to)
{
    this.from = from;
    this.to = to;
    this.color = color(145,187,10);

    this.draw = function()
    {
        strokeWeight(1.5);
        stroke(this.color);
        line(this.from.position.x + this.from.radius/2, this.from.position.y,
            this.to.position.x - this.to.radius/2, this.to.position.y);
    }
}