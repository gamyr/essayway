let head = document.getElementsByTagName("head")[0]
head.innerHTML = `script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
`

const root = document.getElementById("root")
class navlinks extends React.Component {
    render() {
        return (
            <ul style = "list-style-type: none; margin: 0; padding: 0; overflow: hidden; background-color: #f3f3f3; font-family: \"Lato\", sans-serif; ">
                <li style="float:left">
                    <a href="/">Home</a>
                </li>
                <li style="float:left">
                    <a href="/prompts.html">Prompt Generation</a>
                </li>
                <li style="float:left">
                    <a href="/write.html">Writing Editor</a>
                </li>
                <li style="float:left">
                    <a href="/feedback.html">Feedback</a>
                </li>
            </ul>
        )
    }
}