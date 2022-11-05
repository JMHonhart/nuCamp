
const Partner = ({ partner }) => {
    if (partner) {
        const { image, name, description } = partner
        return (
            <>
                <img src={image} alt={name} style={{ width: '150px' }} />
                <h5 className='fw-bold'>{name}</h5>
                {description}
            </>
        )
    }
    return null
}

export default Partner