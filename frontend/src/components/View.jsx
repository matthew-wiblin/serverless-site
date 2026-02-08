import { Title, Card, Text, Image, Grid, Divider, Center } from '@mantine/core';

export default function View({ viewData }) {
  const title = viewData?.title;
  const titlesize = viewData?.titlesize;
  const border = viewData?.border
  const components = viewData?.components;

  function renderTitle() {
    return <Title order={titlesize}>{title}</Title>
  }

  function parentDivProps() {
    const props = {}
    border ? props.style = { border: '1px solid #ccc', borderRadius: '20px', padding: '10px'} : null
    return props
  }

  function renderComponents() {
    return Array.isArray(components) ? components.map((component, index) => renderComponent(component, index)) : null
  }

  function renderComponent(component, index) {
    switch (component.type) {
      case 'card':
        return (
          <Card key={index}>
            <Title key={`card-title-${index}`} order={3}>{component.title}</Title>
            {component.description.map((line, i) => (<Text key={`card-description-${index}-${i}`}>{line}</Text>))}
          </Card>
        )

      case 'photo':
        if (component.where === 'frontend') return <Image key={index} src={`${component.location}`} h='auto' w={500}/>

      case 'divider':
        return <Divider key={index}/>

      case 'grid':
        return component.components.map((row, rowIndex) => {
          const span = 12 / row.length
          return (
            <Grid key={`${index}-row-${rowIndex}`}>
              {row.map((col, colIndex) => (
                <Grid.Col key={`${index}-${rowIndex}-${colIndex}`} span={span}>
                  <Center style={{ flexDirection: 'column' }}>
                    {col.map((child, childIndex) => renderComponent(child, `${index}-${rowIndex}-${colIndex}-${childIndex}`))}
                  </Center>
                </Grid.Col>
              ))}
            </Grid>
          )
        })
      
      default:
        return null
      
    }
  }

  return (
    <div key={`view-${title}`} {...parentDivProps()}>
      {renderTitle()}
      {renderComponents()}
    </div>
  );
}
